from colorama import Fore, Style


class Shape:
    def __init__(self, color: str = "white") -> None:
        self.color = color

    def area(self) -> float:
        raise NotImplementedError("Метод 'area()' должен быть переопределен в подклассе")

    def perimeter(self) -> float:
        raise NotImplementedError("Метод 'perimeter()' должен быть переопределен в подклассе")

    def info(self) -> str:
        return f"{self.get_color(self.color)}{self.color}{Style.RESET_ALL}"  # Цвет слова

    @staticmethod
    def get_color(color_name: str) -> str:
        colors = {
            "red": Fore.RED,
            "blue": Fore.BLUE,
            "green": Fore.GREEN,
            "yellow": Fore.YELLOW,
            "cyan": Fore.CYAN,
            "magenta": Fore.MAGENTA,
            "white": Fore.WHITE
        }
        return colors.get(color_name.lower(), Fore.WHITE)  # Если цвет неизвестен, будет белый


class Square(Shape):
    def __init__(self, side: float, color: str = "white") -> None:
        super().__init__(color)
        self.side = side

    def area(self) -> float:
        return self.side ** 2

    def perimeter(self) -> float:
        return self.side * 4


class Cube(Square):
    def __init__(self, side: float, color: str = "white") -> None:
        super().__init__(side, color)

    def perimeter(self) -> float:
        return super().perimeter() * 4

    def volume(self) -> float:
        return self.side ** 3

    def surface_area(self) -> float:
        return 6 * self.area()


class Parallelepiped(Shape):
    def __init__(self, side1: float, side2: float, side3: float, color: str = "white") -> None:
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def volume(self) -> float:
        return self.side1 * self.side2 * self.side3

    def surface_area(self) -> float:
        return 2 * (self.side1 * self.side2 + self.side1 * self.side3 + self.side2 * self.side3)


# Создаем экземпляры с разными цветами
parallelepiped = Parallelepiped(2, 3, 4, "red")
square = Square(3, "blue")
cube = Cube(3, "green")

# Определяем цвет чисел
number_color = Fore.CYAN

# Вывод результатов с цветами
print(f"CLASS square.\n"
      f"Цвет: {square.info()}\n"
      f"Сторона: {number_color}{square.side}{Style.RESET_ALL}\n"
      f"Площадь: {number_color}{square.area()}{Style.RESET_ALL}\n"
      f"Периметр: {number_color}{square.perimeter()}{Style.RESET_ALL}\n")
print(f"CLASS cube.\n"
      f"Цвет: {cube.info()}\n"
      f"Площадь: {number_color}{cube.area()}{Style.RESET_ALL}\n"
      f"Периметр: {number_color}{cube.perimeter()}{Style.RESET_ALL}\n"
      f"Сторона: {number_color}{cube.side}{Style.RESET_ALL}\n"
      f"Объем: {number_color}{cube.volume()}{Style.RESET_ALL}\n"
      f"Площадь поверхности: {number_color}{cube.surface_area()}{Style.RESET_ALL}\n")
print(f"CLASS parallelepiped.\n"
      f"Цвет: {parallelepiped.info()}\n"
      f"perimeter: {number_color}{parallelepiped.perimeter()}{Style.RESET_ALL}\n"
      f"Объем: {number_color}{parallelepiped.volume()}{Style.RESET_ALL}\n"
      f"Площадь поверхности: {number_color}{parallelepiped.surface_area()}{Style.RESET_ALL}")
