# sample 1
import random

members = ["Василий", "Евгений", "Олег", "София", "Инна", "Василиса", "Петр"]


# print(random.choice(members))

# pr1

def sum_digits(num):
    if num == 0:
        return 0
    return num % 10 + sum_digits(num // 10)


def loop_without_break():
    a = 0
    while a == 0:
        number = random.randint(100, 999)
        if sum_digits(number) == 15:
            print(f"{number} sum = {sum_digits(number)}")
        elif number % 10 == 0:
            print(f"{number} sum = {sum_digits(number)}, Zero")
        elif number % 2 == 0:
            print(f"{number} sum = {sum_digits(number)}, last digit {number % 10}")
            a += 1


def loop_with_break():
    while True:
        number = random.randint(100, 999)
        if sum_digits(number) != 15:
            continue
        if number % 10 == 0:
            print(f"{number} sum = {sum_digits(number)}, Zero")
        elif number % 2 == 0:
            print(f"{number} sum = {sum_digits(number)}, last digit {number % 10}")
            break
        else:
            print(f"{number} sum = {sum_digits(number)}")


# loop_without_break()
# loop_with_break()

# pr2
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)

def factorial(n):
    f = n
    while n > 1:
        n -= 1
        f *= n
    return f

# number_f = int(input("Enter number: "))

# print(f"Factorial {number_f} = {factorial(number_f)}")
