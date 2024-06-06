import openai as ai
import os
from unidecode import unidecode

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

client = ai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = [{"role":"user",
             "content": f"""Escolha aleatoriamente uma palavra em uma lista de palavras aleatórias 
             para uma rodada do jogo da forca. Responda somente com A PALAVRA,
             nada mais, nada menos. A palavra deve a dificuldade: difícil"""}]

response = client.chat.completions.create(
    messages = prompt,
    model = "gpt-3.5-turbo-0125",
    max_tokens = 100,
    temperature = 1
)

print(response.choices[0].message.content.upper())
"""
palavra = "PROgram43-;.+aÇÃO".upper() # response.choices[0].message.content.upper()
print(palavra)
palavra = "".join(filter(str.isalpha, palavra))
print(palavra)
palavra = unidecode(palavra)
print(palavra)"""