import json
import openai as ai
import os
from openai import OpenAI

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

client = ai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Mock
def obter_tempratura_atual(local: str, unidade="celsius") -> dict:
    """Função Mock para pegar a temperatura atual de uma cidade

    Args:
        local (str): Cidade
        unidade (str, optional): Unidade de Medida. Defaults to "celsius".

    Returns:
        dict: Informações da Temperatura
    """
    if "missal" in local.lower():
        return json.dumps({"local":"Missal",
                           "temperatura": "16",
                           "unidade": unidade})
    elif "russas" in local.lower():
        return json.dumps({"local":"Russas",
                           "temperatura": "38",
                           "unidade": unidade})
    elif "são josé dos pinhais" in local.lower():
        return json.dumps({"local":"São José dos Pinhais",
                           "temperatura": "5",
                           "unidade": unidade})
    else:
        return json.dumps({"local": local,
                           "temperatura": "desconhecida"})


tools = [{
    "type": "function",
    "function": {
      "name": "obter_tempratura_atual",
      "description": "Obtém a temperatura atual em uma dada cidade",
      "parameters": {
        "type": "object",
        "properties": {
          "local": {"type": "string","description": "O Nome da cidade. Ex: São José dos Pinhais",},
          "unidade": {"type": "string", "enum": ["celsius", "fahrenheit"]},
        },
        "required": ["local"],
      },
    },
  }]


funcoes_disponiveis = {"obter_tempratura_atual": obter_tempratura_atual}

prompt = [{"role": "user",
             "content": "Qual é a temperatura atual em Missal e Russas? E em Maceió?"}]

response = client.chat.completions.create(
    messages = prompt,
    model = "gpt-3.5-turbo-0125",
    tools = tools,
    tool_choice = "auto"
)

tool_calls = response.choices[0].message.tool_calls

if tool_calls:
    prompt.append(response.choices[0].message)
    for tool_call in tool_calls:
        
        function_name = tool_call.function.name
        function_to_call = funcoes_disponiveis[function_name]
        function_args = json.loads(tool_call.function.arguments)
        function_response = function_to_call(local = function_args.get("local"), unidade = function_args.get("unidade"))
        
        prompt.append({
            "tool_call_id":  tool_call.id,
            "role": "tool",
            "name": function_name,
            "content": function_response
        })
    
response = client.chat.completions.create(
    messages = prompt,
    model = "gpt-3.5-turbo-0125",
)

print(response.choices[0].message.content)
