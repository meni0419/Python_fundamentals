"""
Напишите функцию get_response(url), которая отправляет GET-запрос по заданному URL-адресу и возвращает объект ответа. Затем выведите следующую информацию об ответе:

- Код состояния (status code)
- Текст ответа (response text)
- Заголовки ответа (response headers)

Пример использования:"""

import requests


def get_response(url):
    return requests.get(url)


url = "https://google.com"

response = get_response(url)
print("\033[1;32mStatus Code:\033[0m", response.status_code)
print("\033[1;32mResponse Text:\033[0m", response.text)
print("\033[1;32mResponse Headers:\033[0m", response.headers)
