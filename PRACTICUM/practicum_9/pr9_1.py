"""
1. Дано натуральное число N. Выведите все числа от 1 до N используя рекурсию.
"""


def print_numbers(n):
    if n == 1:
        print(n)
    else:
        print_numbers(n - 1)
        print(n)


print_numbers(5)
