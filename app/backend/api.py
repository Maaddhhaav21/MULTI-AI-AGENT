from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from app.core.ai_agent import get_response_from_ai_agents
from app.config.settings import settings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException


logger = get_logger(__name__)

app = FastAPI(
    title="MULTI AI AGENT",
    version="1.0.0"
)


class RequestState(BaseModel):
    model_name: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "MULTI AI AGENT"
    }


@app.post("/chat")
def chat_endpoint(request: RequestState):

    logger.info(
        f"Received request | model={request.model_name} "
        f"| search={request.allow_search}"
    )

    # Check model
    if request.model_name not in settings.ALLOWED_MODEL_NAMES:

        logger.warning(
            f"Invalid model requested: {request.model_name}"
        )

        raise HTTPException(
            status_code=400,
            detail={
                "error": "Invalid model name",
                "requested_model": request.model_name,
                "allowed_models": settings.ALLOWED_MODEL_NAMES
            }
        )

    try:

        response = get_response_from_ai_agents(
            request.model_name,
            request.messages,
            request.allow_search,
            request.system_prompt
        )

        logger.info(
            f"Successfully generated response "
            f"using {request.model_name}"
        )

        return {
            "response": response
        }

    except Exception as e:

        logger.exception(
            "Error while generating AI response"
        )

        raise HTTPException(
            status_code=500,
            detail=str(
                CustomException(
                    "Failed to get AI response",
                    error_detail=e
                )
            )
        )