from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain_community.chat_message_histories import RedisChatMessageHistory
from langchain.memory import ConversationBufferMemory

import os

llm = ChatOpenAI(temperature=0.7, model="gpt-4", openai_api_key=os.getenv("OPENAI_API_KEY"))

# Tool
def calculator_tool(input: str) -> str:
    try:
        return str(eval(input))
    except:
        return "Invalid math expression"

tools = [
    Tool(
        name="Calculator",
        func=calculator_tool,
        description="Useful for math calculations. Input should be a valid math expression.",
    ),
]

# 👇 Memory using Redis
def get_agent_with_memory(user_id: str):
    message_history = RedisChatMessageHistory(
        session_id=f"user:{user_id}",
        url=os.getenv("REDIS_URL", "redis://localhost:6379"),
    )
    memory = ConversationBufferMemory(
        memory_key="chat_history", return_messages=True, chat_memory=message_history
    )

    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        memory=memory,
    )
    return agent

# Entrypoint
async def run_agent(prompt: str, user_id: str = "user123") -> str:
    agent = get_agent_with_memory(user_id)
    return agent.run(prompt)
