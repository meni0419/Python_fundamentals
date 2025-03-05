"""
2. Напишите программу, которая принимает строку от пользователя и подсчитывает количество уникальных символов
в этой строке. Создайте функцию count_unique_chars, которая принимает строку и возвращает количество уникальных символов.
Выведите результат на экран.

Пример вывода:
Введите строку: hello
Количество уникальных символов: 4
"""

def count_unique_chars(u_str: str) -> int:
    return len(set(u_str.lower()))

text = input("Введите строку: ")
print("Количество уникальных символов (set):", count_unique_chars(text))

"""СО СЛОВАРЕМ"""

def count_unique_chars_2(u_str: str) -> int:
    chars_count = {}
    for char in u_str.lower():
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1
    return len(chars_count)

print("Количество уникальных символов (dict):", count_unique_chars_2(text))

"""GPT учит крутым штукам"""

def count_unique_chars_3(u_str: str) -> int:
    return len({char: u_str.lower().count(char) for char in u_str.lower()})

# Пример использования
print("Количество уникальных символов:(comprehension)", count_unique_chars_3(text))

from collections import Counter

def count_unique_chars_4(u_str: str) -> int:
    return len(Counter(u_str.lower()))

# Пример использования
print("Количество уникальных символов (Counter):", count_unique_chars_4(text))