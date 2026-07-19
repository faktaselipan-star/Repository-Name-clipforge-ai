from fastapi import FastAPI

app = FastAPI(
    title="ClipForge AI",
    description="Open Source AI Video Clipping Platform",
    version="0.1.0"
)


@app.get("/")
async def home():
    return {
        "project": "ClipForge AI",
        "status": "running",
        "version": "0.1.0"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }