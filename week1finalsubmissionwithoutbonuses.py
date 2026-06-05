import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

def run_chosen_chatbot():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    print("Choose a model:")
    print("1. openai/gpt-4o-mini")
    print("2. deepseek/deepseek-chat")
    print("3. google/gemini-2.0-flash-001")
    chosen_model = input("Enter model name: ")
    N = int(input("How many turns to remember (N): "))
   
    print("Chat started. Type 'exit' to quit.\n")
    

    while True:
        
        
        user_text=input("you: ")
        if user_text=="exit":
            break
        messages.append({"role": "user", "content": user_text})

        response=client.chat.completions.create(
            model=chosen_model,
            messages=messages
        )

        reply=response.choices[0].message.content
        print("Assistant:", reply)
        messages.append({"role": "assistant", "content": reply})

        if len(messages)>1+2*N:
            messages.pop(1)
            messages.pop(1)

if __name__ == "__main__":
    run_chosen_chatbot() 