"""
Напишите программу, которая считывает 5 чисел с клавиатуры и записывает их в
текстовый файл.
"""


def read_write_file(filename):
    with open(filename, "w") as file:
        for i in range(5):
            file.write(input("Enter number: ") + " ")
        file.close()
    print("File created")


read_write_file("numbers.txt")
