from fastapi import APIRouter
from pydantic import BaseModel
from app.vector_store.faiss_store import query_vector_store

router = APIRouter()

class QueryInput(BaseModel):
    query: str

@router.post("/query")
async def semantic_search(request: QueryInput):
    response = query_vector_store(request.query)
    return {"results": response}
