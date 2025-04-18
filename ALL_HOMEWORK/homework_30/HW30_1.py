"""
Создайте класс Rectangle для представления прямоугольника.
Класс должен иметь атрибуты width (ширина) и height (высота) со значениями по умолчанию,
а также методы calculate_area() для вычисления площади прямоугольника и calculate_perimeter()
для вычисления периметра прямоугольника.
Переопределить методы __str__, __repr__.
Затем создайте экземпляр класса Rectangle и выведите информацию о нем, его площадь и периметр."""


class Rectangle:
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Прямоугольник {self.width} x {self.height}, площадь: {self.calculate_area()}, периметр: {self.calculate_perimeter()}"

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


rectangle_default = Rectangle()

print(f"Area: {rectangle_default.calculate_area()}, "
      f"Perimeter: {rectangle_default.calculate_perimeter()}")

# Вывод информации об объекте через __str__
print(str(rectangle_default))

# Вывод представления объекта через __repr__
print(repr(rectangle_default))
