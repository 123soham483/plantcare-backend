# PlantCare AI — production-style container for Render.com and other PaaS hosts
FROM python:3.10-slim

# Prevent Python from writing .pyc files and buffer stdout/stderr for cleaner logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# System libraries commonly required by OpenCV wheels and TensorFlow runtime
RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-0 \
    libgomp1 \
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
