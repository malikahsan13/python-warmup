from crewai import Agent, Task, Crew
from langchain.llms import OpenAI
import os

# Set your OpenAI key
os.environ["OPENAI_API_KEY"] = "sk-..."  # Replace with your key

# Create agents
researcher = Agent(
    role="AI Researcher",
    goal="Find the latest insights on AI safety",
    backstory="An expert in analyzing the risks and safety of AI systems",
    verbose=True,
    llm=OpenAI(temperature=0)
)

writer = Agent(
    role="Technical Writer",
    goal="Create a clear, concise report on AI safety",
    backstory="An experienced writer who can summarize complex topics for decision-makers",
    verbose=True,
    llm=OpenAI(temperature=0.5)
)

# Assign tasks to agents
research_task = Task(
    description="Search online sources and summarize key findings about AI safety.",
    agent=researcher
)

write_task = Task(
    description="Write a 1-paragraph summary report based on the researcher's findings.",
    agent=writer,
    depends_on=[research_task]
)

# Create the crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    verbose=True
)

# Run the crew
result = crew.kickoff()
print("\n📝 Final Report:\n", result)
