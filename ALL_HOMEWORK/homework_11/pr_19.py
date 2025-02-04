"""Используя f-строки, спросить имя и возраст, вывести:
"Привет ..., тебе ... лет".
"""


def who_how_where():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print("Hello, my name is {}. I am {} years old.".format(name, age))
    print(f"Hello, my name is {name}. I am {age} years old.")


who_how_where()

"""Пользователь вводит свои параметры в формате имя-фамилия-пол-возраст
(где пол принимает значения “м” или “ж”)
После обработки этой информации программа выводит строку,
где указаны имя и фамилия пользователя, а также средний возраст всех людей такого же пола,
информация о которых была введена ранее:
“Здравствуйте, Иван Иванов!
Средний возраст всех мужчин в нашей БД - 55.22 лет”
Реализовать без хранения списков или иных массивов в памяти.

Данные для предварительного заполнения БД:
"""
data_users = """
Иван-Иванов-м-30
Сергей-Сергеев-м-32
Александр-Александров-м-28
Михаил-Михайлов-м-35
Мария-Маркова-ж-27
Ольга-Петрова-ж-30
Екатерина-Васильева-ж-25
Иван-Иванов-м-12
"""

# text = 'Bearer command: curl - X GET http://127.0.0.1:8000/employees/ -H \"Authorization: Bearer some_token\"'
# word = 'Bearer'
#
#
# def find_indices(text, word):
#     index_found = []
#     i = 0
#     while i < len(text):
#         i = text.lower().find(word.lower(), i)
#         if i == -1:
#             break
#         index_found.append(i)
#         i += len(word)
#     return index_found
#
#
# # print(*find_indices(text, word))
#
#
# def find_indices2(text, word):
#     index_found = ""
#     i = 0
#     while i < len(text):
#         i = text.lower().find(word.lower(), i)
#         if i == -1:
#             break
#         index_found += str(i) + " "
#         i += len(word)
#     return index_found

# print(find_indices2(text, word))
