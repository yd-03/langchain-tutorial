import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

response = openai.ChatCompletion.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "user", "content": "Hello! I'm Bob."},
        {
            "role": "assistant",
            "content": "Nice to meet you, Bob! How can I assist you today?",
        },
        {"role": "user", "content": "Please introduce yourself."},
    ],
    temperature=0,
)

print(response)
