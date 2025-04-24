"""Даны четыре функции (см репозиторий).
Необходимо написать декоратор @timer_execution,
который позволит замерить время их работы.
"""

import time


def tmp(*args):
    """Функция-пустышка, используем для анпакинга итераторов,
    для "exhausting the iterator" ("израсходывания итераторов")
    """


def timer_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время работы функции {func.__name__}: {execution_time:.4f}")

    return wrapper

@timer_execution
def create_with_map(num):
    for _ in range(num):
        x = map(lambda n: 'a' * n, range(num))
        tmp(*x)


@timer_execution
def create_with_list_compr(num):
    for _ in range(num):
        x = ['a' * n for n in range(num)]
        tmp(*x)


@timer_execution
def create_with_generator_expression(num):
    for _ in range(num):
        x = ('a' * n for n in range(num))
        tmp(*x)


@timer_execution
def create_with_loop(num):
    for _ in range(num):
        x = []
        for n in range(num):
            x.append('a' * n)
        tmp(*x)


n_max = 3000
create_with_map(n_max)
create_with_list_compr(n_max)
create_with_generator_expression(n_max)
create_with_loop(n_max)

# Время работы функции create_with_map:  0.0000
# Время работы функции create_with_lst_compr:  0.0000
# Время работы функции create_with_generator_expression:  0.00000
# Время работы функции create_with_loop:  0.00000
