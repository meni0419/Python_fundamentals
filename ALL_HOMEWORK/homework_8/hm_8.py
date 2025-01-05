from math import pow

# So much easy :)
#
# def palindrome(s):
#     return s == s[::-1]

"""
1. Напишите программу, которая запрашивает у пользователя целое число и определяет, является ли оно палиндромом.
Число является палиндромом, если оно читается одинаково слева направо и справа налево.
Выведите соответствующее сообщение на экран с помощью команды print. Используйте математические операции.
Работу со строками использовать нельзя.
"""


def palindrome_hard(n):
    r_digit = 0
    number = n
    while n > 0:
        r_digit = r_digit * 10 + n % 10
        n = n // 10
    return number == r_digit


num = int(input("Enter number: "))
print(f"Is {num} palindrome? {palindrome_hard(num)}")

"""
2. Напишите программу, которая запрашивает у пользователя целое число и проверяет, является ли оно числом Армстронга. 
Число Армстронга - это число, которое равно сумме своих цифр, возведенных в степень, равную количеству цифр в числе. 
Выведите соответствующее сообщение на экран с помощью команды print.
"""


def armstrong(n):
    digit_sum = 0
    number = n
    i = 0
    while n > 0:
        digit_sum += pow((n % 10), len(str(number)))
        n = n // 10
        i += 1
    return digit_sum == number


num = int(input("Enter number: "))
print(f"Is {num} armstrong number? {armstrong(num)}")
