"""
Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы и уровень заголовков,
а затем использует библиотеку Beautiful Soup для парсинга HTML и извлекает заголовки нужного уровня
(теги h1, h2, h3 и т.д.) с их текстом.
"""

from bs4 import BeautifulSoup
import requests

web_adress = input("Enter web address e.g. https://webbuh.com: ")
level = int(input("Enter level of headers e.g. 1: "))

response = requests.get(web_adress)
soup = BeautifulSoup(response.text, "html.parser")

all_h = soup.find_all(f"h{level}")

for h in all_h:
    h = h.get_text()
    print(h)