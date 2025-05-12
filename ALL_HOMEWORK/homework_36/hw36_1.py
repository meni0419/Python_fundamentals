"""
Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы, использует библиотеку Beautiful Soup
для парсинга HTML и выводит список всех ссылок на странице.
"""

from bs4 import BeautifulSoup
import requests

web_adress = input("Enter web address e.g. https://google.com: ")

response = requests.get(web_adress)
soup = BeautifulSoup(response.text, "html.parser")

all_a = soup.find_all('a')

for a in all_a:
    a = a.get('href')
    print(a)