""" 03 ==============================================================================================================
Существует функция coffee(), которая варит кофе
и если ее вызвать, то она печатает "Сварить кофе"

Создайте 4 декоратора так, чтобы в итоге каждый из них добавлял бы
к слову "кофе" следующие фразы:
    - с сахаром,
    - молоком
    - с сахаром и молоком
    - двойной

Вызов декорируемой функции с декоратором (с декораторами)
в итоге должен выводить печатать то, с чем именно кофе сварено

Сварить кофе двойной с сахаром и молоком
Сварить кофе с сахаром и молоком
Сварить кофе с молоком

и так далее.

Представьте, что у вас есть класс Coffee с полем цена и название. Декорировать этот класс по аналогии с предыдущей задачей, чтобы можно было получить кофе с молоком (стоит дороже), кофе с сахаром (цена остается такой же), двойной кофе (цена удваивается).

"""
from functools import wraps


def with_sugar(func):
    def wrapper():
        result = func()
        return result.replace("кофе", "кофе с сахаром")

    return wrapper


def with_milk(func):
    def wrapper():
        result = func()
        return result.replace("кофе", "кофе с молоком")

    return wrapper


def with_milk2(func):
    @wraps(func)
    def wrapper(*args):
        name, price = args

        name = str(name) + " with_milk"
        price += 6
        return func(name, price)

    return wrapper


@with_milk2
def coffee_wm(name, price):
    return f"Сварить кофе {name}: {price}"


print(coffee_wm("latte2", 33))
print(coffee_wm("espresso", 20))


def with_sugar_and_milk(func):
    def wrapper():
        result = func()
        return result.replace("кофе", "кофе с сахаром и молоком")

    return wrapper


def double_coffee(func):
    def wrapper():
        result = func()
        return result.replace("кофе", "кофе двойной")

    return wrapper


# Базовая функция для создания кофе
def coffee():
    return "Сварить кофе"


# Примеры использования декораторов
@with_milk
@double_coffee
def coffee1():
    return coffee()


@with_sugar
@double_coffee
def coffee2():
    return coffee()


@with_sugar_and_milk
def coffee3():
    return coffee()


print(coffee1())  # Сварить кофе двойной с молоком
print(coffee2())  # Сварить кофе двойной с сахаром
print(coffee3())  # Сварить кофе с сахаром и молоком

print("\n# Реализация с использованием класса Coffee")


# Класс Coffee с полями цена и название
class Coffee:
    def __init__(self, name="кофе", price=50):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Сварить {self.name}: {self.price}"


# Функция-декоратор для добавления сахара
def with_sugar_class(cls):
    class NewCoffee(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.name += " с сахаром"
            # Цена не меняется

    return NewCoffee


# Функция-декоратор для добавления молока
def with_milk_class(cls):
    class NewCoffee(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.name += " с молоком"
            self.price += 5

    return NewCoffee


# Функция-декоратор для добавления сахара и молока
def with_sugar_and_milk_class(cls):
    class NewCoffee(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.name += " с сахаром и молоком"
            self.price += 5

    return NewCoffee


# Функция-декоратор для двойного кофе
def double_coffee_class(cls):
    class NewCoffee(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.name += " двойной"
            self.price *= 2

    return NewCoffee


# Применение декораторов к классу
@with_milk_class
@double_coffee_class
class MilkDoubleCoffee(Coffee):
    pass


@with_sugar_class
@double_coffee_class
class SugarDoubleCoffee(Coffee):
    pass


@with_sugar_and_milk_class
class SugarMilkCoffee(Coffee):
    pass


# Примеры использования
print(MilkDoubleCoffee())
print(SugarDoubleCoffee())
print(SugarMilkCoffee())
print(SugarMilkCoffee("latte", 50))
