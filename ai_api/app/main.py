# app/main.py
from fastapi import FastAPI
from app.api.v1 import ai

app = FastAPI(title="AI Agent API", version="1.0")

app.include_router(ai.router, prefix="/api/v1/ai")
