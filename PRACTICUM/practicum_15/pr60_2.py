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
import requests
from requests.exceptions import Timeout, RequestException


def param_decorator(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            for i in range(times):
                print(f"Iteration {i + 1}/{times}")
                try:
                    func(*args, **kwargs)
                except Timeout as err:
                    print(f"Timeout occurred: {err}")
                except RequestException as err:
                    print(f"Request Exception occurred: {err}")
            end_time = time.time()
            print(f"Average time for {func.__name__}: {(end_time - start_time) / times:.6f} seconds")

        return wrapper

    return decorator


@param_decorator(5)
def get_request(url: str):
    return requests.get(url, timeout=5).text


get_request('https://google.com')

# Iteration 1/5
# Iteration 2/5
# Iteration 3/5
# Iteration 4/5
# Iteration 5/5
# Average time for get_request: 0.767245 seconds
