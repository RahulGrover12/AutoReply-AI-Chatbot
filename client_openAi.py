from openai import OpenAI

client = OpenAI(
        api_key="YOUR_API_KEY"
    )
def aiProcess(command):
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a person named Rahul Grover who speaks Hinglish and you are from India and a boy. You Analyze the chat history and respond like Rahul Grover and don't give long answers and use one emoji sometimes. Output should be next chat response as Rahul Grover, text message only so don't respond like Rahul Grover: "},
                {
                    "role": "user",
                    "content": command
                }
            ]
        )
        return(completion.choices[0].message.content)
    
    except Exception as e:
        return("Sorry")
    