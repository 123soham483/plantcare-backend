# PlantCare AI — Plant Disease Detection API

Backend service for **PlantCare AI**, a plant disease detection system built as a FastAPI application. It loads a TensorFlow **MobileNetV2**-style classifier (`plant_disease_model.h5`, reported validation accuracy **94.12%**) trained on **38** classes from the [New Plant Diseases Dataset](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset) (`vipoooool/new-plant-diseases-dataset`).

The API accepts leaf or plant images, returns the top predicted class with a confidence score, and enriches the response with structured agronomic guidance from `solutions.py`.

## Features

- **POST `/predict`** — multipart image upload (JPG, JPEG, PNG), 224×224 resize, pixel values scaled to **[0, 1]**, batch inference, JSON response with plant name, disease name, health flag, confidence, description, treatment steps, and prevention tips.
- **GET `/health`** — API and model load status for monitoring.
- **GET `/diseases`** — all class names (sorted by index from `class_indices.json`).
- **CORS** — open to any origin for a separate React frontend (wildcard origins; see `main.py` for notes on credentials).

## Project layout

```text
plantcare-backend/
├── main.py                 # FastAPI application
├── solutions.py            # DISEASE_INFO for all 38 classes
├── requirements.txt
├── Dockerfile
├── README.md
└── model/
    ├── plant_disease_model.h5
    └── class_indices.json   # {"Class___Name": index, ...}
```

Place your trained **`.h5`** model and **`class_indices.json`** inside the `model/` directory before running. The JSON must map **class name → integer index**; the server reverses this map to decode `argmax` outputs.

## Run locally

### 1. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

**Windows (PowerShell)**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add the model files

Ensure `model/plant_disease_model.h5` and `model/class_indices.json` exist.

### 4. Start the API

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open interactive docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## API reference

### `GET /health`

Returns JSON such as:

```json
{
  "status": "ok",
  "api": "PlantCare AI",
  "model_loaded": true,
  "num_classes": 38
}
```

### `GET /diseases`

Returns every class label (dataset string format), ordered by index:

```json
{
  "count": 38,
  "classes": ["Apple___Apple_scab", "..."]
}
```

### `POST /predict`

- **Body:** `multipart/form-data` with a field named **`file`** (type: image).
- **Allowed types:** `.jpg`, `.jpeg`, `.png` (validated by extension and/or `Content-Type`).

**Example (curl)**

```bash
curl -X POST "http://127.0.0.1:8000/predict" ^
  -H "accept: application/json" ^
  -F "file=@path\to\leaf.jpg"
```

**Example response**

```json
{
  "plant_name": "Tomato",
  "disease_name": "Early blight",
  "is_healthy": false,
  "confidence": 0.9412,
  "description": "...",
  "solution": "1. ...\n2. ...",
  "prevention": "• ...\n• ..."
}
```

**Common errors**

| Status | Meaning |
|--------|---------|
| 400 | Wrong file type, empty file, or undecodable image |
| 500 | Preprocessing or model inference failure |
| 503 | Model/metadata not loaded (misconfiguration) |

## Deploy on Render.com

1. Push this repository to GitHub (or GitLab / Bitbucket) with `Dockerfile` at the repository root.
2. In the Render dashboard, create a **Web Service** and connect the repository.
3. Select **Docker** as the environment; Render will build from the `Dockerfile`.
4. **Important:** Your `plant_disease_model.h5` may exceed Git LFS or git host limits. Options include:
   - Storing the model in cloud object storage and downloading it in a **Render shell** or a **release-phase script** (advanced), or
   - Using a smaller artifact / compressed model if acceptable for your course constraints, or
   - Hosting the model in a private bucket and extending startup code to fetch it (not included by default in this template).
5. Set **Instance type** large enough for TensorFlow inference (free tiers may be tight on RAM).
6. Render sets the **`PORT`** environment variable; the provided `CMD` already binds `uvicorn` to `${PORT:-8000}`.
7. After deploy, test **`GET /health`** on your Render URL, then **`POST /predict`** from your React app (enable your frontend origin in CORS if you later restrict `allow_origins`).

### Docker (local smoke test)

```bash
docker build -t plantcare-api .
docker run --rm -p 8000:8000 -v "%cd%/model:/app/model" plantcare-api
```

Mount or copy the `model/` directory so the container can read the `.h5` and JSON files.

## Academic note

Automated plant disease models can be wrong on unusual lighting, blur, or out-of-distribution crops. Use results for learning and decision support, not as a sole substitute for expert diagnosis.

## License

Use and adapt for your semester project per your institution’s academic integrity rules.
