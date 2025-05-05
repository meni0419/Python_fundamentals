"""
Напишите функцию extract_emails(text), которая извлекает все адреса электронной почты из заданного текста и возвращает их в виде списка.


Пример использования:"""
import re


def extract_emails(text_: str) -> list:
    return re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text_)
    # return re.findall(r"[\w\.-]+@[\w\.-]+", text)


text = "Contact us at info@example.com or support@example.com for assistance."

emails = extract_emails(text)

print(emails)  # Вывод: ['info@example.com', 'support@example.com']
