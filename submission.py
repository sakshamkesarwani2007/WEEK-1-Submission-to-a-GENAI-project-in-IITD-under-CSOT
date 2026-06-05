
#setup

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)


#function


def run_chosen_chatbot():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    print("Choose a model:")
    print("1. openai/gpt-4o-mini")
    print("2. deepseek/deepseek-chat")
    chosen_model = input("Enter model name: ")
    N = int(input("How many turns to remember (N): "))
    
    print("Chat started. Type /compact to store summary. Type 'exit' to quit.\n")
    



#making it remember


    while True:
        user_text=input("you: ")
        if user_text=="exit":
            break


        messages.append({"role": "user", "content": user_text})

        response=client.chat.completions.create(
            model=chosen_model,
            messages=messages,
            stream=True
        )

        
        print("Assistant",end=" ",flush=True)
        reply=""
        for chunk in response:
            token=chunk.choices[0].delta.content or ""
            print(token,end=" ",flush=True)
            reply+=token
        print()  #this is just so that the last end doesnt cause the next you to appear right after assistant message

        messages.append({"role": "assistant", "content": reply})

        if len(messages)>1+2*N or user_text=='/compact':
            history=" ".join(m['content'] for m in messages[1:])
            resp = client.chat.completions.create(
                model=chosen_model,
                messages=[{"role": "user", "content": f"Summarize this conversation concisely:\n{history}"}]
            )
            summary = resp.choices[0].message.content
            messages = [
                messages[0],
                {"role": "assistant", "content": f"Summary of earlier conversation: {summary}"}
            ]

if __name__ == "__main__":
    run_chosen_chatbot() 