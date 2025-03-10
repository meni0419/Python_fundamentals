"""1. Напишите программу, которая подсчитывает количество вхождений каждого слова в тексте и выводит на экран наиболее часто встречающиеся слова. Для решения задачи используйте класс Counter из модуля collections. Создайте функцию count_words, которая принимает текст в качестве аргумента и возвращает словарь с количеством вхождений каждого слова. Выведите наиболее часто встречающиеся слова и их количество.

Пример вывода:
Введенный текст: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est.
sed: 2
Lorem: 1
"""
from collections import Counter
from pprint import pprint


def count_words(string: str) -> dict:
    text_lst = string.lower().split()
    return Counter(text_lst)


text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est."
pprint(count_words(text))
