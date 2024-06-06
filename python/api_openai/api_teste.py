from typing import List
import openai as ai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

client = ai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_response(prompt, model = "gpt-3.5-turbo-0125", max_tokens = 500, temperature = 0): # , stream = True):
    response = client.chat.completions.create(messages = prompt,
                                              model = model,
                                              max_tokens = max_tokens,
                                              temperature = temperature)
                                              # stream = stream)
    
    print(response.choices[0].message.content) 
    prompt.append({"role": "assistant", "content": response.choices[0].message.content})
    
    return response

prompt = [{"role": "user",
          "content": "Crie uma estória sobre o Bard, um modelo linguístico da Google está perdido em um universo deterministico."}]
prompt = get_response(prompt)


"""prompt = [{"role":"user",
            "content": "Qual o sentido da vida?"}]

response = client.chat.completions.create(
    messages = prompt,
    model = "gpt-3.5-turbo-0125",
    max_tokens = 500,
    temperature = 1
)

print(response.choices[0].message.content)
prompt.append({"role": "assistant",
               "content": response.choices[0].message.content})

prompt.append({"role": "user",
               "content": "E qual a filosofia de vida mais conhecida/famosa?"})

response = client.chat.completions.create(
    messages = prompt,
    model = "gpt-3.5-turbo-0125",
    max_tokens = 500,
    temperature = 1
)

print(response.choices[0].message.content)
prompt.append({"role": "assistant",
               "content": response.choices[0].message.content})

prompt.append({"role": "user",
               "content": "E o que você acha sobre tudo isso??"})

response = client.chat.completions.create(
    messages = prompt,
    model = "gpt-3.5-turbo-0125",
    max_tokens = 500,
    temperature = 1
)

print(response.choices[0].message.content)
prompt.append({"role": "assistant",
               "content": response.choices[0].message.content})
"""
