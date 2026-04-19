# PlantCare AI — production-style container for Render.com and other PaaS hosts
FROM python:3.10-slim

# Prevent Python from writing .pyc files and buffer stdout/stderr for cleaner logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# System libraries for OpenCV (cv2) + TensorFlow on Debian slim.
# libxcb1 fixes: ImportError: libxcb.so.1: cannot open shared object file
# libgl1 replaces legacy libgl1-mesa-glx on Debian 12+ (Bookworm) slim images
RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    libgtk-3-0 \
    libgl1 \
    libxcb1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Application source, disease knowledge base, and (at build time) any local model files
COPY . .

# Runtime downloads (gdown) write into model/; ensure directory exists if not in repo context
RUN mkdir -p model

EXPOSE 8000

# Render injects PORT at runtime; default to 8000 for local docker run
CMD sh -c "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"
