from app.core.redis import redis_client

async def save_user_prompt(user_id: str, prompt: str):
    key = f"user:{user_id}:prompts"
    await redis_client.lpush(key, prompt)
    await redis_client.ltrim(key, 0, 9)  # Keep last 10 messages

async def get_user_prompt_history(user_id: str) -> list[str]:
    key = f"user:{user_id}:prompts"
    return await redis_client.lrange(key, 0, 9)
