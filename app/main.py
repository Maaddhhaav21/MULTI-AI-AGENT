import threading
import time
import webbrowser
from pathlib import Path

import uvicorn
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles

from app.backend.api import app
from app.common.logger import get_logger
from app.common.custom_exception import CustomException


logger = get_logger(__name__)

load_dotenv()


# Path to frontend folder
FRONTEND_DIR = Path(__file__).resolve().parent / "frontend"


# Serve the frontend
app.mount(
    "/",
    StaticFiles(
        directory=FRONTEND_DIR,
        html=True
    ),
    name="frontend"
)


def run_backend():
    try:
        logger.info("Starting backend + frontend service...")

        uvicorn.run(
            app,
            host="127.0.0.1",
            port=9999
        )

    except Exception as e:
        logger.error("Problem with backend service")
        raise CustomException("Failed to start backend", e)


def open_browser():
    time.sleep(1.5)
    webbrowser.open("http://127.0.0.1:9999")


if __name__ == "__main__":
    try:
        threading.Thread(
            target=open_browser,
            daemon=True
        ).start()

        run_backend()

    except CustomException as e:
        logger.exception(
            f"CustomException occurred: {str(e)}"
        )