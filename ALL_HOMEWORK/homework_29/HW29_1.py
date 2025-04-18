"""
Создайте класс Rectangle для представления прямоугольника.
Класс должен иметь атрибуты width (ширина) и height (высота),
а также метод calculate_area(), который вычисляет площадь прямоугольника.
Затем создайте экземпляр класса Rectangle с заданными значениями ширины и высоты и выведите его площадь.
"""

class Rectangle:
    def __init__(self, width, height):
        self.wifth = width
        self.height = height
    def calculate_area(self):
        return self.wifth * self.height


rectangle_4x5 = Rectangle(4, 5)

print(rectangle_4x5.calculate_area())