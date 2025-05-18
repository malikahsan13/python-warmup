import openai
import json

openai.api_key = "sk-..."  # Replace with your key

# Simulated external function
def get_weather(city: str):
    return {"location": city, "temperature": "22°C", "condition": "Sunny"}

# Function schema
functions = [
    {
        "name": "get_weather",
        "description": "Get weather info for a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "Name of the city"},
            },
            "required": ["city"],
        },
    }
]

# Step 1: Send user prompt and function list
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "What's the weather in Paris?"}
    ],
    functions=functions,
    function_call="auto"
)

# Step 2: Extract function call (if any)
msg = response["choices"][0]["message"]

if msg.get("function_call"):
    func_name = msg["function_call"]["name"]
    arguments = json.loads(msg["function_call"]["arguments"])
    
    # Step 3: Call the tool
    if func_name == "get_weather":
        tool_response = get_weather(arguments["city"])

    # Step 4: Return tool result to GPT for final response
    second_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": "What's the weather in Paris?"},
            msg,  # assistant message with function call
            {
                "role": "function",
                "name": func_name,
                "content": json.dumps(tool_response)
            }
        ]
    )

    print("Assistant:", second_response["choices"][0]["message"]["content"])
else:
    print("Assistant:", msg["content"])
