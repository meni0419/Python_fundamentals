"""02. Напишите генератор, который будет генерировать арифметическую прогрессию

В качестве аргументов генераторной функции передаётся
- начальное значение прогрессии,
- шаг (по умолчанию = 1),
- и последний элемент прогрессии (по умолчанию бесконечная прогрессия)"""


def arithmetic_progression(start, step=1, end=None):
    current = start
    while end is None or current <= end:
        yield current
        current += step


for value in arithmetic_progression(0, 2, 10):
    print(value)
