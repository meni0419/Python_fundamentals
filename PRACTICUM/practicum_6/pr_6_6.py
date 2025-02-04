"""
Создайте текстовый файл persons.txt, где 5 строчек, в каждой есть фамилия;имя;возраст. То
есть каждая строка - информация о человеке и данные разделены точкой с запятой.
Напишите программу, которая вычитывает данные из файла и печатает их на экран в
формате Имя: <имя>, Фамилия <фамилия>, Возраст <возраст>.
"""


def read_print_file(filename):
    list_of_persons = ""
    with open(filename, "r") as file:
        for i in file:
            surname, name, age = i.split(";")
            list_of_persons += "First name: " + name + ", Last name: " + surname + ", Age: " + age
        file.close()
    print(list_of_persons)


read_print_file("persons.txt")

# if using print() inside `for` then added unnecessary extra line
