from bs4 import BeautifulSoup
import re
import requests
import pandas as pd

url = "https://br.investing.com/equities/apple-computer-inc"
page = requests.get(url)

# print(page.status_code) #  Verificando permissão para acessar o código

soup = BeautifulSoup(page.text, "lxml")

current_price = soup.find("div", class_="text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]").text
print(f"Preço Atual: {current_price}.")

closing_price = soup.find("dd", class_="whitespace-nowrap text-[#232526]").text
print(f"Preço de Fechamento do Dia Anterior: {closing_price}.")

price_var = soup.find_all("div", class_="flex items-center gap-2 font-bold tracking-[0.2px]")[1]
price_var = price_var.find_all("span")
price_var_lower, price_var_higher = price_var[0].text, price_var[1].text
print(f"A Variação nas as últimas 52 semanas foi entre: {price_var_lower} e {price_var_higher}.")
