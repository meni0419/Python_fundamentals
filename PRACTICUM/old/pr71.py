"""
Написать программу, которая скачивает страницу с сайта https://bank.gov.ua/ua/markets/exchangerates/
 на выбор с актуальным курсом валют, выделяет курс доллара к евро и выводит его. Можно пользоваться регулярными выражениями и Beautiful Soup вместе.
"""


import requests
from bs4 import BeautifulSoup

url = "https://bank.gov.ua/ua/markets/exchangerates/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'class': 'inner'})

    if table:
        usd_rate = None
        eur_rate = None

        for row in table.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) >= 5:
                currency_code = cells[1].text.strip()
                rate = float(cells[4].text.strip().replace(',', '.'))

                if currency_code == 'USD':
                    usd_rate = rate
                elif currency_code == 'EUR':
                    eur_rate = rate

        if usd_rate and eur_rate:
            usd_to_eur = usd_rate / eur_rate
            print(f"Курс доллара к евро: {usd_to_eur:.4f}")


# AUD (Австралийский доллар): 56,3087
# AZN (Азербайджанский манат): 50,5614
# AMD (Армянских драмов): 22,1686
# BYN (Белорусский рубль): 27,7209
# BGN (Болгарский лев): 47,9690
# BRL (Бразильский реал): 15,2064
# HUF (Венгерских форинтов): 23,5530
# KRW (Вон Республики Корея): 62,6398
# VND (Вьетнамских донгов): 35,4451
# HKD (Гонконгский доллар): 11,0439
# GEL (Грузинский лари): 31,8231
# DKK (Датская крона): 12,5716
# AED (Дирхам ОАЭ): 23,4048
# USD (Доллар США): 85,9543
# EUR (Евро): 93,8419
