"""
Напишите программу, которая принимает список чисел от пользователя и использует функцию reduce из модуля functools,
чтобы найти произведение всех чисел в списке. Затем программа должна использовать функцию itertools.accumulate
для накопления произведений чисел в новом списке. В результате программа должна вывести список,
содержащий накопленные произведения.
"""

from functools import reduce
from itertools import accumulate


def multiply_list(list_num: list) -> tuple:
    multiply_all = reduce(lambda x, y: x * y, list_num)
    multiply_acc = list(accumulate(list_num, lambda x, y: x * y))
    # multiply_acc = list(accumulate([multiply_all] + list_num, lambda x, y: x * y))
    # return multiply_acc
    return f"multiply_all = {multiply_all}", f"multiply_acc = {multiply_acc}"

print(multiply_list([1, 2, 3, 4, 5]))