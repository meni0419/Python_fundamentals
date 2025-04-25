"""
Реализовать класс Email, представляющий электронное письмо. Класс должен поддерживать следующие операции:
- Сравнение писем по дате (операторы <, >, <=, >=, ==, !=)
- Преобразование письма в строку (метод __str__)
- Получение длины текста письма (метод __len__)
- Получение хеш-значения письма (метод __hash__)
- Проверка наличия текста в письме (метод __bool__)
"""

# Пример использования:

email1 = Email("john@example.com", "jane@example.com", "Meeting", "Hi Jane, let's have a meeting tomorrow.", "2022-05-10")

email2 = Email("jane@example.com", "john@example.com", "Re: Meeting", "Sure, let's meet at 2 PM.", "2022-05-10")

email3 = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob, how are you?", "2022-05-09")


print(email1)  # Вывод:

"""

From: john@example.com

To: jane@example.com

Subject: Meeting


Hi Jane, let's have a meeting tomorrow.

"""


print(len(email2))  # Вывод: 24

print(hash(email3))  # Вывод: -920444056

print(bool(email1))  # Вывод: True

print(email2 > email3)  # Вывод: True