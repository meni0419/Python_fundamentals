"""
Реализовать класс Counter, который представляет счетчик. Класс должен поддерживать следующие операции:
- Увеличение значения счетчика на заданное число (оператор +=)
- Уменьшение значения счетчика на заданное число (оператор -=)
- Преобразование счетчика в строку (метод __str__)
- Получение текущего значения счетчика (метод __int__)

Пример использования:
counter = Counter(5)
counter += 3
print(counter)  # Вывод: 8
counter -= 2
print(int(counter))  # Вывод: 6
"""


class Counter:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Counter):
            return Counter(self.value + other.value)
        else:
            return Counter(self.value + other)

    def __isub__(self, other):
        self.value -= other
        return self

    def __sub__(self, other):
        return Counter(self.value - other.value)

    def __str__(self):
        return str(self.value)

    def __int__(self):
        return self.value


counter = Counter(5)
counter += 3
print("counter 5 + 3:", "\033[32m", counter, "\033[0m")

counter2 = Counter(10)
counter3 = Counter(15)
counter4 = Counter(1000)
counter5 = counter2 + counter3 + counter4
print("counter5 (+counter2,3,4):", "\033[32m", counter5, "\033[0m")

counter -= 2
print("counter - 2:", "\033[32m", counter, "\033[0m")
print("call __int__:", "\033[32m", int(counter), "\033[0m")
