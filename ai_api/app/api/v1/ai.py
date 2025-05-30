# app/api/v1/ai.py
from fastapi import APIRouter
from app.models.ai_models import AIRequest, AIResponse
from app.services.openai_service import generate_ai_response


router = APIRouter()

@router.post("/generate", response_model=AIResponse)
async def generate_text(request: AIRequest):
    response = await generate_ai_response(request.prompt, user_id="user123")
    return {"response " : response}