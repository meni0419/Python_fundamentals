"""
Даны два целых числа A и B (при этом A ≤ B). Напишите функцию, которая печатает все
числа от A до B включительно.
"""


def range_func(a, b):
    result = ""
    for i in range(a, b + 1):
        result += str(i) + " "
        i += 1
    print(result)


a= 18
b = 23
range_func(a, b)
# range_func(int(input("Enter first number: ")),
#            int(input("Enter second number: "))
#            )
