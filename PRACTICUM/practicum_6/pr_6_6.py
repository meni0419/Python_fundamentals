"""
Создайте текстовый файл persons.txt, где 5 строчек, в каждой есть фамилия;имя;возраст. То
есть каждая строка - информация о человеке и данные разделены точкой с запятой.
Напишите программу, которая вычитывает данные из файла и печатает их на экран в
формате Имя: <имя>, Фамилия <фамилия>, Возраст <возраст>.
"""


def read_print_file():
    def write_file():
        filename = "persons.txt"
        with open(filename, "w") as file:
            persons_list = """
                Ivanov;Ivan;25
                Petrov;Petr;30
                Sidorov;Sidr;35
                Smirnov;Sergey;28
                Nikolaev;Nikolay;40
            """
            persons_list = persons_list.strip().replace(" ", "")
            file.write(persons_list)
            file.close()

            # for i in range(5):
            #     file.write(input("Enter surname: ") + ";" + input("Enter name: ") + ";" + input("Enter age: ") + "\n")
            # file.close()
        print("File created")
        return filename

    print("File read")
    list_of_persons = ""
    with open(write_file(), "r") as file:
        for i in file:
            surname, name, age = i.split(";")
            list_of_persons += "First name: " + name + ", Last name: " + surname + ", Age: " + age
        file.close()
    return list_of_persons


print(read_print_file())
# print(read_print_file("persons.txt"))

# if using print() inside `for` then added unnecessary extra line
