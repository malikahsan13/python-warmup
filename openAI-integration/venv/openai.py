import openai

openai.api_key = "sk-..."  # Replace with your actual key

def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or "gpt-3.5-turbo" if you're on free tier
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message["content"]

def main():
    print("🤖 GPT Assistant. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        reply = ask_gpt(user_input)
        print(f"Assistant: {reply}\n")

if __name__ == "__main__":
    main()
