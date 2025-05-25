from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
import os

llm = ChatOpenAI(temperature=0.7, model="gpt-4", openai_api_key=os.getenv("OPENAI_API_KEY"))

# Simple tool
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

agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

async def run_agent(prompt: str) -> str:
    return agent.run(prompt)
