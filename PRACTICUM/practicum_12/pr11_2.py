"""Напишите функцию get_largest_string(), которая
 - принимает список строк
 - и возвращает наибольшую строку из списка.
Функция должна быть аннотирована с помощью аннотаций типов.
"""

from typing import List



def get_largest_string2(lst: List[str]) -> str:
    max_len_word = ''
    for word in lst:
        if len(word) > len(max_len_word):
            max_len_word = word
    return max_len_word

def get_largest_string(strings: list[str]) -> str:
    return max(strings, key=len)

lst = ["apple", "banana", "pear", "grape", "orange"]
print(get_largest_string(lst))  # banana

