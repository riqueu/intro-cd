import openai as ai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

ai.api_key=os.getenv("OPENAI_API_KEY")
client = ai.OpenAI(api_key=ai.api_key) # Testar: client = ai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = [{"role":"user",
            "content": "O que é mirrado?"}]

response = client.chat.completions.create(
    messages=prompt,
    model="gpt-3.5-turbo-0125",
    max_tokens=100,
    temperature=0
)

print(response.choices[0].message.content)
"""Mirrado é um adjetivo que se refere a algo ou alguém que está magro, fraco, debilitado ou sem vigor.
Pode ser usado para descrever uma pessoa ou animal que está em estado de desnutrição ou que apresenta
uma aparência frágil e doente. Também pode ser utilizado de forma figurada para descrever algo que é
escasso, limitado ou insuficiente."""