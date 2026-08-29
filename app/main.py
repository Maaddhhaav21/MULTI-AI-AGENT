import threading
import time
import webbrowser
from pathlib import Path

import uvicorn
from fastapi.staticfiles import StaticFiles

from app.backend.api import app
from app.common.logger import get_logger

logger = get_logger(__name__)

# app/main.py -> app/
APP_DIR = Path(__file__).resolve().parent

# app/frontend/
FRONTEND_DIR = APP_DIR / "frontend"

if not FRONTEND_DIR.exists():
    raise RuntimeError(
        f"Frontend directory not found: {FRONTEND_DIR}"
    )

# Serve frontend AFTER the API routes have been registered.
app.mount(
    "/",
    StaticFiles(
        directory=str(FRONTEND_DIR),
        html=True
    ),
    name="frontend"
)


def open_browser():
    time.sleep(1.5)
    webbrowser.open("http://127.0.0.1:9999/")


if __name__ == "__main__":

    logger.info("Starting MULTI-AI-AGENT...")
    logger.info(f"Frontend directory: {FRONTEND_DIR}")
    logger.info("Server: http://127.0.0.1:9999")

    threading.Thread(
        target=open_browser,
        daemon=True
    ).start()

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=9999,
        log_level="info"
    )