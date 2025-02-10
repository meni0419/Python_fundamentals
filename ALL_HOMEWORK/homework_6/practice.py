import random
import timeit


def hour_check(hour=0):
    while hour > 23 or hour < 0:
        hour = int(input("Please, enter hour between 0 and 23:"))
    return hour


# print(hour_check())

# Выберите случайным образом победителя розыгрыша из списка
members = ["Василий", "Евгений", "Олег", "София", "Инна", "Василиса", "Петр"]


def sum_digits(num):
    if num == 0:
        return 0
    return num % 10 + sum_digits(num // 10)


def loop_without_break():
    """1. Для трехзначных чисел оставить только те, сумма цифр в которых равна 15.
       Для четных выводить дополнительно последнюю цифру.
       Для оканчивающихся на ноль печатать строку zero.
       Попробовать решить сначала без break/continue, потом избегая вложенных условий"""
    do_it = True
    while do_it:
        number = random.randint(100, 999)
        if sum_digits(number) == 15:
            print(f"{number} sum = {sum_digits(number)}", end=", ")
            if number % 10 == 0:
                print(f"Zero")
            elif number % 2 == 0:
                print(f"last digit {number % 10}")
            do_it = False


#print(timeit.timeit("loop_without_break", globals=globals(), number=1))


# print(f"\n====second solution====\n")


def loop_with_break():
    while True:
        number = random.randint(100, 999)
        if sum_digits(number) != 15:
            continue
        print(f"{number} sum = {sum_digits(number)}", end=", ")
        if number % 10 == 0:
            print(f"Zero")
        elif number % 2 == 0:
            print(f"last digit {number % 10}")
        break


#print(timeit.timeit("loop_with_break()", globals=globals(), number=1))


def loop_with_break2():
    """1. Для трехзначных чисел оставить только те, сумма цифр в которых равна 15.
       Для четных выводить дополнительно последнюю цифру.
       Для оканчивающихся на ноль печатать строку zero.
       Попробовать решить сначала без break/continue, потом избегая вложенных условий"""
    while True:
        number = random.randint(100, 999)
        if sum_digits(number) != 15 or number % 10 != 0 or number % 2 != 0:
            continue
        print(f"{number} sum = {sum_digits(number)}, last digit {number % 10}, Zero")
        break


# print(timeit.timeit("loop_with_break2()", globals=globals(), number=1))


def loop_with_break3():
    """1. Для трехзначных чисел оставить только те, сумма цифр в которых равна 15.
       Для четных выводить дополнительно последнюю цифру.
       Для оканчивающихся на ноль печатать строку zero.
       Попробовать решить сначала без break/continue, потом избегая вложенных условий"""
    #count = 0
    while True:
        num = 906 #int(input("Enter number: "))
        if sum_digits(num) != 15: #or count==10:
            #count +=1
            continue
        else:
            print(f"{num} sum = {sum_digits(num)}", end=", ")
        if num % 10 == 0:
            print(f"Zero")
        elif num % 2 == 0:
            print(f"last digit {num % 10}")
        break


#number = int(input("Enter number: "))
# print(timeit.timeit("loop_with_break3()", globals=globals(), number=1))


def factorial_es(n):
    if n == 0:
        return 1
    return n * factorial_es(n - 1)


def factorial(n):
    """Напишите программу, которая запрашивает у пользователя положительное целое число и
       вычисляет его факториал.
       Факториал числа N вычисляется как произведение всех целых чисел от 1 до N.
       Используйте цикл с предусловием while для решения задачи.
       Выведите результат на экран с помощью команды print."""
    f = n
    if n == 0:
        return 1
    while n > 1:
        n -= 1
        f *= n
    return f


# number_f = int(input("Enter number: "))
#
# print(f"Factorial {number_f} = {timeit.timeit("factorial(number_f)", globals=globals(), number=5)}")
# print(f"\n====second solution====\n")
# print(f"Factorial {number_f} = {timeit.timeit("factorial_es(number_f)", globals=globals(), number=5)}")

def guess_number(x):
    x = int(input("Enter number: "))
    print("You win!" if x == 42 else "You lose!")


def flip_flop(str_):
    """Реализуйте функцию flip_flop(), которая принимает на вход строку и, если эта строка равна 'flip',
    возвращает строку 'flop'. В противном случае функция должна вернуть 'flip'."""
    return "flop" if str_ == "flip" else "flip"


# print(flip_flop("flip"))
# print(flip_flop("flop"))

def print_num_reverse():
    num_ = input("Enter number: ")
    print(num_[::-1])


# print_num_reverse()

def print_num_reverse2(n):
    while n:
        print(n)
        n -= 1
    else:
        print("Done")

# print_num_reverse2(5)
