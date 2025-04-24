"""
1. Напишите декоратор validate_args, который будет проверять типы аргументов функции и выводить сообщение об ошибке, если переданы аргументы неправильного типа. Декоратор должен принимать ожидаемые типы аргументов в качестве параметров.

Пример использования:
@validate_args(int, str)
def greet(age, name):
    print(f"Привет, {name}! Тебе {age} лет")
greet(25, "Анна") # Все аргументы имеют правильные типы
greet("25", "Анна") # Возникнет исключение TypeError
Ожидаемый вывод:
Привет, Анна! Тебе 25 лет.
TypeError: Аргумент 25 имеет неправильный тип <class 'str'>. Ожидается <class 'int'>."""

#gpt
def validate_args(*expected_types):
    def decorator(func):
        def wrapper(*args):
            for arg, expected_type in zip(args, expected_types):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Аргумент {arg} имеет неправильный тип {type(arg)}. Ожидается {expected_type}")
            return func(*args)

        return wrapper

    return decorator

#my
def validate_args2(type1, type2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                if not isinstance(args[0], type1):
                    raise TypeError(f"Аргумент {args[0]} имеет неправильный тип {type(args[0])}. Ожидается {type1}")
                if not isinstance(args[1], type2):
                    raise TypeError(f"Аргумент {args[1]} имеет неправильный тип {type(args[1])}. Ожидается {type2}")
                return func(*args, **kwargs)
            except TypeError as e:
                print(f"TypeError: {e}")
                return None

        return wrapper

    return decorator


@validate_args2(int, str)
def greet(age, name):
    print(f"Привет, {name}! Тебе {age} лет")


# Корректный вызов:
greet(25, "Анна")

# Ошибочный вызов:
greet("25", "Анна")
