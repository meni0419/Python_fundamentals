# ANSI escape codes for text colors
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"  # Resets the text color to default

print(
    f"""{BLUE}1. Напишите программу, которая принимает список чисел от пользователя и передает его в функцию modify_list, 
    которая изменяет элементы списка. Функция должна умножить нечетные числа на 2, а четные числа разделить на 2. 
    Выведите измененный список на экран. Объясните, почему изменения происходят только внутри функции 
    и как работают изменяемые и неизменяемые параметры.

    Пример вывода:
    Введите список чисел, разделенных пробелами: 1 2 3 4 5
    Измененный список чисел: [2, 1, 6, 2, 10]\n{RESET}""")


def modify_list(numbers):
    numbers = list(map(int, numbers.split()))
    numbers = list(map(lambda number: number // 2 if number % 2 == 0 else number * 2, numbers))
    return numbers


numbers = "1 2 3 4 5"
print(f"Измененный список чисел: {GREEN}{modify_list(numbers)}{RESET}\n")
