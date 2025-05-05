"""
Реализуйте абстрактный базовый класс Shape (фигура), а от него унаследуйте классы Rectangle (прямоугольник) и Circle (круг). Класс Shape должен иметь абстрактный метод area, который должен быть реализован в каждом дочернем классе. Классы Rectangle и Circle также должны иметь метод perimeter для расчета периметра. Выведите площадь и периметр прямоугольника и круга на экран.
Пример
использования:"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError

    @abstractmethod
    def perimeter(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * 3.14 * self.radius


rectangle = Rectangle(5, 3)

circle = Circle(2)

print(f"Rectangle area: {rectangle.area()}")  # Вывод: Rectangle area: 15
print(f"Rectangle perimeter: {rectangle.perimeter()}")  # Вывод: Rectangle perimeter: 16
print(f"Circle area: {circle.area()}")  # Вывод: Circle area: 12.566370614359172
print(f"Circle perimeter: {circle.perimeter()}")  # Вывод: Circle perimeter: 12.566370614359172
