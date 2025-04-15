"""
Напишите функцию, которая принимает на вход список чисел и возвращает сумму квадратов только четных чисел из списка,
используя функциональные подходы (например, map, filter и reduce).

Пример вывода:
Введите числа: 4, 6, 3, 4, 2, 3, 9, 0, 7
Результат: 72"""
from functools import reduce


def even_quarto(list_num: str) -> int:
    list_num = list(map(int, list_num.split(", ")))
    return sum(map(lambda x: x ** 2, filter(lambda y: y % 2 == 0, list_num)))


print(f"Результат: {even_quarto("4, 6, 3, 4, 2, 3, 9, 0, 7")}")
# print(f"Результат: {even_quarto(input("Введите числа через запятую: "))}")
