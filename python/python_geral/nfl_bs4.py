from bs4 import BeautifulSoup
import re
import requests
import pandas as pd

url = "https://www.nfl.com/standings/league/2023/REG"
page = requests.get(url)
soup = BeautifulSoup(page.text, "lxml")

table = soup.find("table", {"summary": "Standings - Detailed View"})
headers = []

for each_element in table.find_all("th"):
    title = each_element.text.strip()
    headers.append(title)

df = pd.DataFrame(columns=headers)

for each_row in table.find_all("tr")[1:]:
    row_data = []
    
    first_td = each_row.find_all("td")[0].find("div", class_="d3-o-club-fullname").text.strip()
    first_td = re.sub(r"\s+", " ", first_td)
    
    row_data.append(first_td)
    
    for each_td in each_row.find_all("td")[1:]:
        row_data.append(each_td.text.strip())
    
    df.loc[len(df)] = row_data

print(df.tail())
df.to_csv("nfl_rip.csv")
