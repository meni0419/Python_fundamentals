"""
1. Напишите программу, которая запрашивает у пользователя строку и определяет, является ли она панграммой.
Панграмма - это фраза, содержащая все буквы алфавита. Программа должна игнорировать регистр букв и пробелы при проверке
панграммы. Выведите соответствующее сообщение на экран с помощью команды print. Решить задачу для латиницы.
"""


def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvxyz"
    s = s.lower()
    s = s.replace(" ", "")
    i = 0
    while i < len(alphabet):
        if alphabet[i] not in s:
            return False
        i += 1
    return True

    # better solution
    # for letter in alphabet:
    #     if letter not in s:
    #         return False
    # return True

"""
2. Напишите программу, которая запрашивает у пользователя строку и выводит на экран количество гласных и согласных букв 
в ней. Используйте функцию len() для подсчета количества букв. Выведите результат на экран с помощью команды print. 
Решить задачу для латиницы.
"""

def count_vowels_and_consonants(s):
    vowels = "aeiouy"
    consonants = "bcdfghjklmnpqrstvwxyz"
    s = s.lower()

    vowels_count = ""
    consonants_count = ""
    i = 0
    while i < len(s):
        if s[i] in vowels:
            vowels_count += s[i]
        elif s[i] in consonants:
            consonants_count += s[i]
        i += 1
    return len(vowels_count), len(consonants_count)

# def count_vowels(s):
#     vowels = "aeiouy"
#     vowels_count = 0
#     for letter in s:
#         if letter in vowels:
#             vowels_count += 1
#     return vowels_count
#
# def count_consonants(s):
#     consonants = "bcdfghjklmnpqrstvwxyz"
#     consonants_count = 0
#     for letter in s:
#         if letter in consonants:
#             consonants_count += 1
#     return consonants_count


u_s = input("Enter string: ")
print(f"1. Is {u_s} pangram? {is_pangram(u_s)}")

vowels_len, consonants_len = count_vowels_and_consonants(u_s)
print(f"2. Count vowels and consonants: {vowels_len} vowels, {consonants_len} consonants")
# pr 1
#
# s = "ABC"
# print(s[0:1])
# print(s[0:2])
# print(s[0:3])

# pr2
#
# def print_all_ascii_table():
#     n = 127
#     while n >= 0:  # ASCII characters range from 127 to 0
#         print(f"{n:3} => {chr(n)}")
#         n -= 1
#
# print_all_ascii_table()
