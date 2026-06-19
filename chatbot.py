from ollama import chat

print("Welcome to Ollama Chatbot")
print("Type 'exit' to quit\n")

while True:
    user_prompt = input("You: ")

    if user_prompt.lower() == "exit":
        print("Goodbye!")
        break

    response = chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    print("\nAI:", response["message"]["content"])
    print()
