import requests
import os
import wikipedia
import json
from bs4 import BeautifulSoup

country = input("country name...")

wikipedia.set_lang('en')
page = wikipedia.page(f"Cities of {country}")


req = requests.get(page.url)
soup = BeautifulSoup(req.text, 'lxml')
table = soup.find_all('table')

first_column_values = []
rows = table[0].find_all('tr')  # Находим все строки таблицы
for row in rows:
    first_cell = row.find('td')  # Находим первую ячейку строки
    if first_cell:  # Проверяем, что ячейка существует
        first_column_values.append(first_cell.get_text(strip=True))

print(first_column_values)
