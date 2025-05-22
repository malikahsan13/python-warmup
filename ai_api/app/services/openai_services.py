# app/services/openai_service.py
import openai
import os
from dotenv import load_dotenv
from app.core.logging_config import logger

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_ai_response(prompt: str) -> str:
    logger.info(f"Generating response for prompt: {prompt[:50]}...")
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        message = completion.choices[0].message["content"]
        logger.info("AI response generated successfully.")
        return message
    except openai.error.OpenAIError as e:
        logger.exception("OpenAI API failure")
        raise
