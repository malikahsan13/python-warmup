# app/main.py
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from app.api.v1 import ai
from app.core.exceptions import (
    validation_exception_handler,
    openai_exception_handler
)
from openai.error import OpenAIError

app = FastAPI(title="AI Agent API", version="1.0")

app.include_router(ai.router, prefix="/api/v1/ai")

# Register custom exception handlers
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(OpenAIError, openai_exception_handler)
