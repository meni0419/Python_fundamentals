"""Дан массив целых чисел длины 1 и более. Написать функцию, которая возвращает массив длины
2, состоящих из первого и последнего элемента входного массива. {1, 2, 3} -> {1, 3}, {7, 4, 6, 2} ->
{7, 2}
Стать IT-шником может каждый ICH
"""


def first_and_last(array):
    return [array[0], array[-1]]


print(first_and_last([1, 2, 3]))
print(first_and_last([7, 4, 6, 2]))


def first_and_last_v2(array):
    return array[:1] + [array[-1]]


print(first_and_last_v2([1, 2, 3]))
print(first_and_last_v2([7, 4, 6, 2]))

"""ну и дальше .extend() и все остальное"""
