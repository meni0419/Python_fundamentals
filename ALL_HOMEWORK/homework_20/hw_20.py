"""1. Напишите функцию merge_dicts, которая принимает произвольное количество словарей
в качестве аргументов и возвращает новый словарь, объединяющий все входные словари.
Если ключи повторяются, значения должны быть объединены в список.
Функция должна использовать аргумент **kwargs для принятия произвольного числа аргументов словаря.

Пример ввода:
{'a': 1, 'b': 2}
{'b': 3, 'c': 4}
{'c': 5, 'd': 6}

Пример вывода:
{'a': [1], 'b': [2, 3], 'c': [4, 5], 'd': [6]}"""


def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        for key, value in d.items():
            if key in result:
                # Append the new value to the existing list
                result[key].append(value)
            else:
                # Create a new list with the current value
                result[key] = [value]
    return result


# Testing the function with multiple dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'c': 5, 'd': 6}

print(merge_dicts(dict1, dict2, dict3))
