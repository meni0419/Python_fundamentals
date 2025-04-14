"""Создать класс Car (машина) со следующими полями: model, year, color."""


class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

car = Car('Golf', 2020, 'Red')

if __name__ == '__main__':
    print(car.model, car.year, car.color)
