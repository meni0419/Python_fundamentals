"""1. Напишите программу, которая открывает файл, считывает из него два числа и выполняет операцию их деления.
Если число отрицательное, выбросите исключение ValueError с сообщением "Число должно быть положительным".
Обработайте исключение и выведите соответствующее сообщение."""
import json


# def divide_pos(a: int, b: int) -> any:
def divide_pos() -> any:
    try:
        with open("22_1.json", "r") as file:
            data = json.load(file)
            a = data["a"]
            b = data["b"]
            if a < 0 or b < 0:
                raise ValueError("Число должно быть положительным")
            print(f"a / b = {a / b}")
    except ValueError as ve:
        print(ve)
    except ZeroDivisionError:
        print("На ноль делить нельзя")

# a_ = 2
# b_ = 2
# divide_pos(a_, b_)

divide_pos()