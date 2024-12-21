import requests
import os
import wikipedia
import json
from bs4 import BeautifulSoup

country = input("country name...")

wikipedia.set_lang('en')
page = wikipedia.page(f"Cities of {country}")
# print(wikipedia.page('Cities of England').url)

req = requests.get(page.url)
soup = BeautifulSoup(req.text, 'lxml')
table = soup.find_all('table')

first_column_values = []
rows = table[0].find_all('tr') 
for row in rows:
    first_cell = row.find('td')
    if first_cell:
        first_column_values.append(first_cell.get_text())

print(first_column_values)
