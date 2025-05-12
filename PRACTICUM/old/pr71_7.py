"""Написать программу, которая скачивает страницу с сайта на выбор
с актуальным курсом валют, выделяет курс доллара к евро и выводит его.
Можно пользоваться регулярными выражениями и Beautiful Soup вместе.

Уточнение: используйте html-код файла <example_table.html>
"""

from bs4 import BeautifulSoup


def get_html(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()

html_content = get_html('example_table.html')
soup = BeautifulSoup(html_content, 'html.parser')

tbody = soup.tbody

for tr in tbody.find_all('tr'):
    if tr.find_all('td')[1].text == 'USD':
        tr.find_all('td')
        usd = float(tr.find_all('td')[4].text.replace(',', '.'))
    if tr.find_all('td')[1].text == 'EUR':
        tr.find_all('td')
        eur = float(tr.find_all('td')[4].text.replace(',', '.'))

print(f'Курс USD / EUR = {usd / eur}')
# AUD Австралийский доллар 58,0043
# AZN Азербайджанский манат 51,7600
# AMD Армянских драмов 22,6655
# BYN Белорусский рубль 28,1601
# BGN Болгарский лев 49,1738

# Курс USD / EUR = 0.9244371976920589
