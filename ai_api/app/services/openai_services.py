# app/services/openai_service.py
import openai
import os
from dotenv import load_dotenv
from app.core.logging_config import logger
from app.services.memory_service import save_user_prompt, get_user_prompt_history

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_ai_response(prompt: str, user_id: str = "default") -> str:
    await save_user_prompt(user_id, prompt)
    
    history = await get_user_prompt_history(user_id)

    messages = [{"role": "user", "content": p} for p in reversed(history)]
    logger.info(f"Context messages: {len(messages)}")

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    return completion.choices[0].message["content"]
