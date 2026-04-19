"""
PlantCare AI — FastAPI backend for plant disease detection.

Loads a TensorFlow MobileNetV2-based classifier (.h5) and serves predictions
for educational / demonstration purposes. Always validate critical agronomic
decisions with qualified experts and local extension services.
"""

from __future__ import annotations

import io
import json
import logging
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any

import cv2
import numpy as np
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import tensorflow as tf
import gdown

from solutions import DISEASE_INFO

# ---------------------------------------------------------------------------
# Dataset label aliases (Kaggle "new-plant-diseases" folder names vs. keys in
# DISEASE_INFO). If your class_indices.json uses the long names on the left,
# we still resolve the same guidance text as the canonical entry on the right.
# ---------------------------------------------------------------------------

CLASS_INFO_ALIASES: dict[str, str] = {
    "Cherry_(including_sour)___Powdery_mildew": "Cherry___Powdery_mildew",
    "Cherry_(including_sour)___healthy": "Cherry___healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": "Corn___Cercospora_leaf_spot",
    "Corn_(maize)___Common_rust_": "Corn___Common_rust",
    "Corn_(maize)___Northern_Leaf_Blight": "Corn___Northern_Leaf_Blight",
    "Corn_(maize)___healthy": "Corn___healthy",
    "Grape___Esca_(Black_Measles)": "Grape___Esca",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": "Grape___Leaf_blight",
    "Orange___Haunglongbing_(Citrus_greening)": "Orange___Haunglongbing",
    "Pepper,_bell___Bacterial_spot": "Pepper___Bacterial_spot",
    "Pepper,_bell___healthy": "Pepper___healthy",
    "Tomato___Spider_mites Two-spotted_spider_mite": "Tomato___Spider_mites",
}

# ---------------------------------------------------------------------------
# Paths and constants
# ---------------------------------------------------------------------------

MODEL_DIR = Path("model")
MODEL_PATH = MODEL_DIR / "plant_disease_model.h5"
CLASS_INDICES_PATH = MODEL_DIR / "class_indices.json"

# Google Drive direct-download URLs (uc?id=...) for Render / Docker cold starts
GDRIVE_MODEL_URL = (
    "https://drive.google.com/uc?id=16x-J6C6JCdXbFW0_d4TIJFmGltOumvZL"
)
GDRIVE_CLASS_INDICES_URL = (
    "https://drive.google.com/uc?id=1FZDgoLgLExfVkw_M4JoN_Y8YJn4NQFfz"
)

# Accepted uploads for /predict (aligned with common mobile / web camera outputs)
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}
ALLOWED_CONTENT_TYPES = {
    "image/jpeg",
    "image/jpg",
    "image/pjpeg",
    "image/png",
    "image/x-png",
}

# Image size expected by MobileNetV2-style classifiers in this project
INPUT_SIZE = (224, 224)

# Global references populated during application lifespan
model: tf.keras.Model | None = None
index_to_class: dict[int, str] = {}

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("plantcare")


def download_from_gdrive() -> None:
    """
    Ensure ``plant_disease_model.h5`` and ``class_indices.json`` exist under ``model/``.

    Uses ``gdown`` with the public ``/uc?id=`` links. Skips download when a file
    already exists (local dev with cached weights). Logs progress to stdout and
    the application logger so platforms like Render capture output.
    """
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    targets: list[tuple[str, Path, str]] = [
        (GDRIVE_MODEL_URL, MODEL_PATH, "plant_disease_model.h5"),
        (GDRIVE_CLASS_INDICES_URL, CLASS_INDICES_PATH, "class_indices.json"),
    ]

    for url, dest, label in targets:
        if dest.is_file():
            msg = f"Model artifact already present, skipping download: {label}"
            logger.info(msg)
            print(f"[PlantCare] {msg}", flush=True)
            continue

        logger.info("Downloading %s from Google Drive → %s", label, dest)
        print(
            f"[PlantCare] Downloading {label} from Google Drive (this may take several minutes)...",
            flush=True,
        )
        try:
            # quiet=False shows tqdm-style progress in logs where supported
            gdown.download(url, str(dest), quiet=False)
        except Exception:
            logger.exception("gdown failed while downloading %s", label)
            raise

        if not dest.is_file():
            raise RuntimeError(
                f"Download finished but file is missing on disk: {dest.resolve()}"
            )

        done = f"Download complete: {label} → {dest}"
        logger.info(done)
        print(f"[PlantCare] {done}", flush=True)


def _build_index_to_class(raw_indices: dict[str, Any]) -> dict[int, str]:
    """
    Reverse Keras-style class_indices.json mapping {class_name: index}
    into {index: class_name} for argmax decoding.
    """
    mapping: dict[int, str] = {}
    for class_name, idx in raw_indices.items():
        try:
            mapping[int(idx)] = str(class_name)
        except (TypeError, ValueError) as exc:
            raise ValueError(
                f"Invalid class index for '{class_name}': {idx!r}"
            ) from exc
    if not mapping:
        raise ValueError("class_indices.json produced an empty index map")
    return mapping


def load_model_and_indices() -> tuple[tf.keras.Model, dict[int, str]]:
    """
    Load the serialized Keras model and class index metadata from disk.

    Raises:
        FileNotFoundError: if required files are missing.
        ValueError: if JSON structure is invalid.
        Exception: propagates TensorFlow model load failures.
    """
    if not MODEL_PATH.is_file():
        raise FileNotFoundError(f"Model file not found: {MODEL_PATH.resolve()}")
    if not CLASS_INDICES_PATH.is_file():
        raise FileNotFoundError(
            f"Class indices file not found: {CLASS_INDICES_PATH.resolve()}"
        )

    logger.info("Loading TensorFlow model from %s", MODEL_PATH)
    try:
        # compile=False skips recompilation and avoids failures on newer Keras
        # when the saved config contains unknown keys (e.g. quantization_config).
        loaded = tf.keras.models.load_model(
            MODEL_PATH,
            compile=False,
        )
    except Exception:
        logger.exception("TensorFlow failed to load model")
        raise

    logger.info("Loading class indices from %s", CLASS_INDICES_PATH)
    with CLASS_INDICES_PATH.open("r", encoding="utf-8") as f:
        raw = json.load(f)
    if not isinstance(raw, dict):
        raise ValueError("class_indices.json must contain a JSON object")

    idx_map = _build_index_to_class(raw)
    expected = len(idx_map)
    if expected != 38:
        logger.warning(
            "Expected 38 classes for this project; found %s in class_indices.json",
            expected,
        )
    return loaded, idx_map


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan: load ML assets at startup so requests fail fast
    if the deployment is misconfigured.
    """
    global model, index_to_class
    try:
        download_from_gdrive()
        model, index_to_class = load_model_and_indices()
    except FileNotFoundError as fnf:
        logger.error("%s", fnf)
        raise
    except Exception as exc:
        logger.error("Startup failed while loading model or indices: %s", exc)
        raise
    logger.info("Model loaded successfully")
    yield
    # Optional cleanup (TensorFlow manages most resources automatically)
    model = None
    index_to_class = {}
    logger.info("PlantCare AI shutdown complete")


app = FastAPI(
    title="PlantCare AI",
    description="Plant disease detection API powered by TensorFlow MobileNetV2",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS: allow any origin for a decoupled React / SPA frontend during development
# and typical student deployments. Tighten origins in production if required.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # Wildcard origins cannot be combined with credentials=True (browser CORS rule).
    # Use explicit allow_origins + allow_credentials=True if you need cookie auth later.
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


def _validate_image_upload(filename: str | None, content_type: str | None) -> None:
    """Reject unsupported media types before decoding bytes."""
    suffix = Path(filename or "").suffix.lower()
    ctype = (content_type or "").split(";")[0].strip().lower()

    ext_ok = suffix in ALLOWED_EXTENSIONS
    mime_ok = ctype in ALLOWED_CONTENT_TYPES

    if not (ext_ok or mime_ok):
        raise HTTPException(
            status_code=400,
            detail=(
                "Invalid file type. Only JPG, JPEG, and PNG uploads are supported. "
                f"Received filename={filename!r}, content_type={content_type!r}"
            ),
        )


def preprocess_image(image_bytes: bytes) -> np.ndarray:
    """
    Decode and preprocess an image for MobileNetV2-style inference.

    Steps:
        1. Decode image robustly (OpenCV primary; PIL fallback).
        2. Convert to RGB if needed.
        3. Resize to 224×224.
        4. Normalize pixel values to the [0, 1] range (float32).
        5. Expand batch dimension: shape (1, 224, 224, 3).

    Args:
        image_bytes: Raw bytes from multipart upload.

    Returns:
        Numpy array of shape (1, 224, 224, 3), dtype float32.

    Raises:
        HTTPException: 400 if bytes cannot be decoded as an image.
    """
    if not image_bytes:
        raise HTTPException(status_code=400, detail="Empty image upload")

    # Try OpenCV imdecode first (uses project dependency opencv-python)
    arr = np.frombuffer(image_bytes, dtype=np.uint8)
    decoded = cv2.imdecode(arr, cv2.IMREAD_COLOR)

    if decoded is None:
        # Fallback: some PNG/JPEG variants decode more reliably via Pillow
        try:
            pil_img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
            rgb = np.array(pil_img, dtype=np.uint8)
        except Exception as exc:
            logger.info("Image decode failed: %s", exc)
            raise HTTPException(
                status_code=400,
                detail="Could not decode image. Ensure a valid JPG or PNG file.",
            ) from exc
    else:
        rgb = cv2.cvtColor(decoded, cv2.COLOR_BGR2RGB)

    resized = cv2.resize(rgb, INPUT_SIZE, interpolation=cv2.INTER_AREA)
    normalized = resized.astype(np.float32) / 255.0
    batch = np.expand_dims(normalized, axis=0)
    return batch


def _fallback_info(predicted_class: str) -> dict[str, Any]:
    """Safe metadata if a class string is missing from DISEASE_INFO (should not happen)."""
    parts = predicted_class.split("___", 1)
    plant = parts[0].replace("_", " ") if parts else "Unknown plant"
    disease = parts[1].replace("_", " ") if len(parts) > 1 else predicted_class
    is_healthy = "healthy" in predicted_class.lower()
    return {
        "plant_name": plant,
        "disease_name": disease,
        "is_healthy": is_healthy,
        "description": (
            "Automated information is not available for this exact class label. "
            "Consult a plant pathologist or agricultural extension service."
        ),
        "solution": (
            "1. Collect additional clear photos of affected and healthy tissue.\n"
            "2. Note cultivar, growth stage, and recent weather.\n"
            "3. Seek expert diagnosis before applying treatments."
        ),
        "prevention": (
            "• Use certified planting material.\n"
            "• Scout regularly and keep records.\n"
            "• Follow integrated pest management guidelines for your region."
        ),
    }


@app.get("/health", tags=["System"])
async def health() -> dict[str, Any]:
    """
    Lightweight readiness probe for orchestrators (e.g., Render, Docker health checks).

    Returns:
        JSON with API status and whether the model is loaded in memory.
    """
    ready = model is not None and bool(index_to_class)
    return {
        "status": "healthy" if ready else "unhealthy",
        "api": "PlantCare AI",
        "model_loaded": ready,
        "num_classes": len(index_to_class) if index_to_class else 0,
    }


@app.get("/diseases", tags=["Metadata"])
async def list_diseases() -> dict[str, Any]:
    """
    Enumerate all class labels exactly as stored in class_indices.json,
    sorted by numeric index for stable ordering.
    """
    if not index_to_class:
        raise HTTPException(status_code=503, detail="Class metadata not loaded yet")
    ordered = [index_to_class[i] for i in sorted(index_to_class.keys())]
    return {"count": len(ordered), "classes": ordered}


@app.post("/predict", tags=["Inference"])
async def predict(file: UploadFile = File(...)) -> dict[str, Any]:
    """
    Run disease classification on a single leaf or plant image.

    Request:
        multipart/form-data with field name `file` (jpg, jpeg, or png).

    Response:
        JSON containing plant and disease names, health flag, confidence,
        and agronomic guidance strings sourced from `solutions.DISEASE_INFO`.
    """
    if model is None or not index_to_class:
        raise HTTPException(
            status_code=503,
            detail="Model is not available. Check server logs and model/ paths.",
        )

    _validate_image_upload(file.filename, file.content_type)

    try:
        raw_bytes = await file.read()
    except Exception as exc:
        logger.exception("Failed to read upload")
        raise HTTPException(
            status_code=400, detail="Could not read uploaded file"
        ) from exc

    try:
        batch = preprocess_image(raw_bytes)
    except HTTPException:
        raise
    except Exception as exc:
        logger.exception("Unexpected preprocessing error")
        raise HTTPException(
            status_code=500, detail="Image preprocessing failed"
        ) from exc

    try:
        predictions = model.predict(batch, verbose=0)
        probs = np.asarray(predictions[0], dtype=np.float64)
        pred_idx = int(np.argmax(probs))
        confidence = float(np.max(probs))
        predicted_class = index_to_class.get(pred_idx)
        if predicted_class is None:
            logger.error("Model argmax index %s not in index_to_class", pred_idx)
            raise HTTPException(
                status_code=500,
                detail="Prediction index out of range for configured classes",
            )
    except HTTPException:
        raise
    except Exception as exc:
        logger.exception("Model inference failed")
        raise HTTPException(
            status_code=500,
            detail="Model inference failed. Verify model compatibility and input shape.",
        ) from exc

    canonical = CLASS_INFO_ALIASES.get(predicted_class, predicted_class)
    info = DISEASE_INFO.get(canonical)
    if info is None:
        logger.warning(
            "No DISEASE_INFO entry for class: %s (canonical=%s)",
            predicted_class,
            canonical,
        )
        base = _fallback_info(predicted_class)
    else:
        base = dict(info)

    # Confidence is returned explicitly for transparency / UI gauges
    response = {
        "plant_name": base["plant_name"],
        "disease_name": base["disease_name"],
        "is_healthy": bool(base["is_healthy"]),
        "confidence": round(confidence, 6),
        "description": base["description"],
        "solution": base["solution"],
        "prevention": base["prevention"],
    }
    return response
