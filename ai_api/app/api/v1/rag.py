from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.rag_agent import get_rag_response

router = APIRouter()

class QueryInput(BaseModel):
    query: str

@router.post("/ask")
async def ask_question(input: QueryInput):
    answer = get_rag_response(input.query)
    return {"response": answer}
