"""Дано два массива целых чисел. Написать функцию, которая возвращает true, если их первые или
последние элементы равны. Оба массива минимальной длины 1.
"""


def compare_first_last_p7_2(array_1, array_2):
    return array_1[0] == array_2[0] or array_1[-1] == array_2[-1]


array_1 = [1, 2, 3]
array_2 = [3, 3, 3]

print(compare_first_last_p7_2(array_1, array_2))
