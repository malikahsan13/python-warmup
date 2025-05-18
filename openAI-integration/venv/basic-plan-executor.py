import openai
import wikipedia
import json

openai.api_key = "sk-..."  # Replace with your OpenAI key

# Tool: search Wikipedia
def search_wikipedia(topic):
    try:
        summary = wikipedia.summary(topic, sentences=3)
        return {"result": summary}
    except Exception as e:
        return {"error": str(e)}

# Define available tools
functions = [
    {
        "name": "search_wikipedia",
        "description": "Search and summarize a topic using Wikipedia",
        "parameters": {
            "type": "object",
            "properties": {
                "topic": {"type": "string", "description": "Topic to search"},
            },
            "required": ["topic"],
        },
    }
]

# User request
user_input = "Tell me about Artificial Intelligence."

# Step 1: Ask GPT what tool to use
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": user_input}],
    functions=functions,
    function_call="auto"
)

msg = response["choices"][0]["message"]

if msg.get("function_call"):
    func_name = msg["function_call"]["name"]
    args = json.loads(msg["function_call"]["arguments"])

    if func_name == "search_wikipedia":
        tool_result = search_wikipedia(args["topic"])

        # Step 2: Feed tool output back into GPT for final answer
        final_response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": user_input},
                msg,
                {"role": "function", "name": func_name, "content": json.dumps(tool_result)}
            ]
        )

        print("🤖 AI Agent:", final_response["choices"][0]["message"]["content"])
else:
    print("🤖 AI Agent:", msg["content"])
