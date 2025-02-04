"""
1. Напишите программу, которая запрашивает у пользователя число N и выводит на экран таблицу умножения от 1 до N.
Используйте вложенный цикл for для создания таблицы умножения. Выведите результат на экран с помощью команды print.
"""


def multiplication_table():
    num = int(input("Enter number: "))
    str_r_table = ""
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            r_table = i * j
            str_r_table += str(r_table) + "\t"
        print(f"{str_r_table}")
        str_r_table = ""


multiplication_table()

"""
2. Напишите программу, которая принимает два списка одинаковой длины и создает новый список, содержащий пары элементов
из исходных списков. Используйте функцию zip() для создания пар элементов. Выведите результат на экран с помощью команды
print.
"""


def create_pairs():
    list1 = "1 2 3 4 5"
    list2 = "A B C D E"

    print(list(zip(list1.split(" "), list2.split(" "))))


create_pairs()
