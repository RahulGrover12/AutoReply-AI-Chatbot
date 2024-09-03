import os

from groq import Groq

client = Groq(
    api_key="YOUR_API_KEY",
)
chat_completion = client.chat.completions.create(
    messages=[
       {"role": "system", "content": "You are a person who speaks Hinglish and he is from India. You Analyze the chat history and respond like that person. It should feel like that person is responding so analyze carefully and reply according to that only."},
            {
                "role": "user",
                "content": "command",
            }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)