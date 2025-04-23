"""
Напишите декоратор log_args, который будет записывать аргументы и результаты вызовов функции в лог-файл. Каждый вызов функции должен быть записан на новой строке в формате "Аргументы: <аргументы>, Результат: <результат>". Используйте модуль logging для записи в лог-файл.

Пример использования:
python
@log_args
def add(a, b):
    return a + b

add(2, 3)
add(5, 7)

Ожидаемый вывод в файле log.txt:
Аргументы: 2, 3, Результат: 5
Аргументы: 5, 7, Результат: 12

Убедитесь, что перед запуском кода у вас создан файл log.txt в той же директории, где находится скрипт Python."""
import logging
import os


def log_args(func):
    if not os.path.exists("log.txt"):
        raise FileNotFoundError("File 'log.txt' not found")

    logging.basicConfig(
        filename='log.txt',
        level=logging.INFO,
        format='%(message)s'
    )

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"Аргументы: {', '.join(map(str, args))}, Результат: {result}")
        return result

    return wrapper


@log_args
def add(a, b):
    return a + b


add(2, 3)
add(5, 7)
