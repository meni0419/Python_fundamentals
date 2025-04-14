"""02 ===============================================
Создайте список из 10 объектов этого класса,
описывающих модели разных марок, лет и цветов.
Используйте для этого следующие данные:
"""

data = [
    ('Golf', 2020, 'Red'),
    ('Toyota', 2019, 'Blue'),
    ('Polo', 2021, 'Green'),
    ('Alfa-Romeo', 2018, 'Black'),
    ('Skoda', 2022, 'Red'),
    ('Touareg', 2017, 'Yellow'),
    ('Sharan', 2016, 'Red'),
    ('Phaeton', 2015, 'Gold'),
    ('BMV', 2014, 'Brown'),
    ('Nissan', 2013, 'Red')
]


class Car:
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color


cars = [Car(brand, year, color) for brand, year, color in data]
for car in cars:
    print(car.brand, car.year, car.color)
