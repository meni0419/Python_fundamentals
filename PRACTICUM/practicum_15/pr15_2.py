""" 02 ======================================================================================================
Импортировать классы фигур из предыдущего файла.

Составить список, содержащий по 2 экземпляра каждого класса фигуры.
Вывести на печать площадь каждого объекта в формате:
Area of Circle(name=circle, radius=5): 78.54
с точностью до 2-го знака после запятой
"""
from pr15_1 import Circle, Square, Rectangle


figures = [
    Circle('Circle', 5),
    Circle('circle', 3),
    Square('square', 4),
    Square('square', 6),
    Rectangle('rectangle', 3, 4),
    Rectangle('rectangle', 5, 6)
]

def print_area(figure):
    print(f"Area of {figure}: {figure.calculate_area():.2f}")

for figure in figures:
    print_area(figure)

# Area of Circle(name=circle, radius=5): 78.54
# Area of Circle(name=circle, radius=3): 28.27
# Area of Square(name=square, side=4): 16.00
# Area of Square(name=square, side=6): 36.00
# Area of Rectangle(name=rectangle, side1=3, side2=4): 12.00
# Area of Rectangle(name=rectangle, side1=5, side2=6): 30.00