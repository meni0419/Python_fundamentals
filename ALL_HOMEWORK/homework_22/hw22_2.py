"""2. Напишите программу, которая открывает файл, считывает его содержимое
и выполняет операции над числами в файле. Обработайте возможные исключения
при открытии файла (FileNotFoundError) и при выполнении операций над числами
(ValueError, ZeroDivisionError). Используйте конструкцию try-except-finally
для обработки исключений и закрытия файла в блоке finally."""
import json


def main():
    try:
        with open("22_2.json", "r") as file:
            data = json.load(file)
            a = data["a"]
            b = data["b"]
            try:
                print(f"a + b = {a + b}")
                print(f"a - b = {a - b}")
                print(f"a * b = {a * b}")
                print(f"a / b = {a / b}")
            except ZeroDivisionError:
                print("На ноль делить нельзя")
            finally:
                file.close()
                print("File was closed")
    except FileNotFoundError as fnf:
        print(f"FileNotFoundError: {fnf}")


main()
