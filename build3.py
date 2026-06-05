import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "My name is Saksham."},
    {"role": "user", "content": "What is my name?"},
]

resp = client.chat.completions.create(model="openai/gpt-4o-mini", messages=messages)
print(resp.choices[0].message.content)
