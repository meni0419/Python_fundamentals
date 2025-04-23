"""Создать декоратор, который замеряет время работы функции.
Предусмотреть различное число итераций для сглаживания показателя.

Пример:
@param_decorator(5)
def get_request(url: str):
    return requests.get(url).text

get_request('https://google.com')

pip install requests
"""
import time
import random


def param_decorator(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            for i in range(times):
                print(f"Iteration {i+1}/{times}")
                func(*args, **kwargs)
            end_time = time.time()
            print(f"Average time for {func.__name__}: {(end_time - start_time)/times:.6f} seconds")
        return wrapper
    return decorator


@param_decorator(5)
def get_request():
    x = random.randint(0, 2)
    time.sleep(x)
    print(f"   Delay is {x} seconds")


get_request()

# Iteration 1/5
#    Delay is 2 seconds
# Iteration 2/5
#    Delay is 2 seconds
# Iteration 3/5
#    Delay is 0 seconds
# Iteration 4/5
#    Delay is 2 seconds
# Iteration 5/5
#    Delay is 0 seconds
# Average time for get_request: 1.200120 seconds
