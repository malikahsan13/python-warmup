from fastapi import APIRouter
from app.schemas.ai import AIRequest, AIResponse
from app.agents.simple_agent import run_agent

router = APIRouter()

@router.post("/run", response_model=AIResponse)
async def run_langchain_agent(request: AIRequest):
    user_id = "user123"  # Replace this with request.user_id if you add auth
    output = await run_agent(request.prompt, user_id=user_id)
    return {"response": output}
