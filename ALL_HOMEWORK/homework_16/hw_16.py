# ANSI escape codes for text colors
from unittest.util import sorted_list_difference

RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"  # Resets the text color to default

print(
    f"""{BLUE}1. Напишите программу, которая принимает матрицу (вложенный список) от пользователя и находит сумму 
    всех элементов в матрице. Используйте вложенные списки и циклы для обхода элементов матрицы.

    Пример матрицы: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Пример вывода: Сумма элементов в матрице: 45{RESET}\n""")


def sum_of_elements(matrix):
    sum_matrix = 0
    for row in matrix:
        for element in row:
            sum_matrix += element
    return sum_matrix


input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(f"Сумма элементов в матрице: {GREEN}{sum_of_elements(input_matrix)}{RESET}")

print(
    f"""{BLUE}\n2. Напишите программу, которая принимает список чисел от пользователя и сортирует его в порядке убывания, 
    используя метод sort() и параметр reverse=True. Выведите отсортированный список на экран.

    Пример вывода:
    Введите список чисел, разделенных пробелами: 5 2 8 1 3
    Отсортированный список чисел: [8, 5, 3, 2, 1]{RESET}\n""")


def sort_list():
    numbers = input("Введите список чисел, разделенных пробелами: ")
    s_num = list(map(int, numbers.split()))
    s_num.sort(reverse=True)
    return s_num

print(f"Отсортированный список чисел: {GREEN}{sort_list()}{RESET}")
