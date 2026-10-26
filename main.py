from ollama import chat

def main():
    print("Welcome to Local AI Assistant!")
    print("GPU: NVIDIA RTX 5080")
    print("Initializing local AI assistant...")

    question = input("Ask your local AI something: ")

    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    print("\nAI:", response.message.content)

if __name__ == "__main__":
    main()