"""
1. Напишите функцию find_longest_word, которая будет принимать список слов и возвращать самое длинное слово из списка. Аннотируйте типы аргументов и возвращаемого значения функции.

Пример вызова функции и ожидаемого вывода:
words = ["apple", "banana", "cherry", "dragonfruit"]
result = find_longest_word(words)
print(result)  # Ожидаемый вывод: "dragonfruit"
"""

def find_longest_word(lst: list[str]) -> str:
    return max(lst, key=len)

words = ["apple", "banana", "cherry", "dragonfruit"]
result = find_longest_word(words)
print(result)