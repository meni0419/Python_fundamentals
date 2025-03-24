"""1. Напишите программу, которая генерирует и выводит квадраты чисел от 1 до N с использованием генераторного выражения. Реализуйте функцию generate_squares, которая принимает число N в качестве аргумента и использует генераторное выражение для генерации квадратов чисел. Затем выведите квадраты чисел на экран.

Пример работы программы:
1
4
9
16
25"""


def generate_squares(n: int):
    """Генерирует квадраты чисел от 1 до N."""
    for x in range(1, n + 1):
        yield x ** 2


# Пример вызова
N = 5
squares_gen = generate_squares(N)

for square in squares_gen:
    print(square)

"""2. Напишите генератор, который будет генерировать бесконечную последовательность Фибоначчи. Каждый раз, когда генератор вызывается, он должен возвращать следующее число последовательности. Напишите программу, которая будет использовать этот генератор для вывода первых N чисел Фибоначчи.
Пример вывода:

Введите количество чисел Фибоначчи: 10
Первые 10 чисел Фибоначчи:
0
1
1
2
3
5
8
13
21
34
"""


def fibonacci_generator():
    """Генератор бесконечной последовательности Фибоначчи."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Использование генератора
N = int(input("Введите количество чисел Фибоначчи: "))
print(f"Первые {N} чисел Фибоначчи:")
fib_gen = fibonacci_generator()
for i in range(N):
    print(next(fib_gen))
