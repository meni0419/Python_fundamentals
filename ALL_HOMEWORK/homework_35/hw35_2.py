"""
Напишите функцию find_common_words(url_list), которая принимает список URL-адресов и возвращает список наиболее часто встречающихся слов на веб-страницах. Для каждого URL-адреса функция должна получить содержимое страницы с помощью запроса GET и использовать регулярные выражения для извлечения слов. Затем функция должна подсчитать количество вхождений каждого слова и вернуть наиболее часто встречающиеся слова в порядке убывания частоты."""

import requests
from bs4 import BeautifulSoup
from collections import Counter

def find_common_words(url_list):
    words = []
    for url in url_list:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text()
        words.extend(text.lower().split())
    return Counter(words).most_common()

url_list = ["https://en.wikipedia.org/wiki/Ana_de_Armas", "https://en.wikipedia.org/wiki/Tom_Hardy"]

print(find_common_words(url_list))