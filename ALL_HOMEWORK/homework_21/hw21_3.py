"""
3. Напишите программу, которая принимает словарь от пользователя и ключ, и возвращает значение для указанного ключа с использованием метода get или setdefault. Создайте функцию get_value_from_dict, которая принимает словарь и ключ в качестве аргументов, и возвращает значение для указанного ключа, используя метод get или setdefault в зависимости от выбранного варианта. Выведите полученное значение на экран.

Пример словаря:
my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}

Пример вывода:
Введите ключ для поиска: banana
Использовать метод get (y/n)? y
Значение для ключа 'banana': 6
"""


def get_value_from_dict(dictionary: dict, key: str, use_get: str) -> dict:
    if use_get == 'y':
        return dictionary.get(key)
    else:
        return dictionary.setdefault(key)

my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
key_ = input("Введите ключ для поиска: ")
use_get_ = input("Использовать метод get (y/n)? ")
print(f"Значение для ключа '{key_}': {get_value_from_dict(my_dict, key_, use_get_)}")