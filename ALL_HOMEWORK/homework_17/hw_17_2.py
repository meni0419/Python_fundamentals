# ANSI escape codes for text colors
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"  # Resets the text color to default

print(
    f"""{BLUE}2. Напишите программу, которая принимает произвольное количество аргументов от пользователя 
    и передает их в функцию calculate_sum, которая возвращает сумму всех аргументов. 
    Используйте оператор * при передаче аргументов в функцию. Выведите результат на экран.

    Пример вывода:
    Введите числа, разделенные пробелами: 1 2 3 4 5
    Сумма чисел: 15\n{RESET}""")


def calculate_sum(*args):
    return sum(args)


a = "1"
b = "2"
c = "3"
d = "4"
e = "5"

# input_args = input("Введите числа, разделенные пробелами: ")
# print(f"Сумма чисел: {GREEN}{calculate_sum(*list(map(int, input_args.split())))}")
print(calculate_sum(int(a), int(b), int(c), int(d), int(e)))
