# app/main.py
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from app.api.v1 import ai
from app.core.exceptions import (
    validation_exception_handler,
    openai_exception_handler
)
from openai.error import OpenAIError
from app.core.db import init_db
from app.api.v1 import agent


app = FastAPI(title="AI Agent API", version="1.0")

@app.on_event("startup")
async def startup_event():
    await init_db()

app.include_router(ai.router, prefix="/api/v1/ai")
app.include_router(agent.router, prefix="/api/v1/agent")

# Register custom exception handlers
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(OpenAIError, openai_exception_handler)
