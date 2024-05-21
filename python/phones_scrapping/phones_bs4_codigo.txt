from bs4 import BeautifulSoup
import re
import requests
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"
page = requests.get(url)
soup = BeautifulSoup(page.text, "lxml")

# Queremos: Product Name, Description, Price, Reviews

table = soup.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")
headers = ["Product Name", "Description", "Price", "Reviews"]
df = pd.DataFrame(columns=headers)

for each_phone in table:
    product_name = each_phone.find(class_="title").text.strip()
    description = each_phone.find(class_="description card-text").text.strip()
    price = each_phone.find(class_="price float-end card-title pull-right").text.strip()
    reviews = each_phone.find(class_="ratings").text.strip()
    row_data = [product_name, description, price, reviews]
    df.loc[len(df)] = row_data

df.to_csv("phones_rip.csv")
