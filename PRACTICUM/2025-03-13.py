"""Функция принимает текст и возвращает словарь, где
    ключи - символы, из которых состоит тест,
    значения - их количество.

Решите задачу с помощью collections.Counter

Пример:
get_statistics("Python is the best!")

# {'P': 1, 'y': 1, 't': 3, 'h': 2, 'o': 1, 'n': 1, ' ': 3, 'i': 1, 's': 2, 'e': 2, 'b': 1, '!': 1}
"""
import json
from collections import Counter


def get_statistics(text: str) -> dict:
    return Counter(text)


# txt = "Python is the best!"
# print(get_statistics(txt))


"""Дан список именованных тюплов.
Необходимо распечатать каждую строку в формате:
Country: France, Capital: Paris, Population: 67 mln
"""

from collections import namedtuple

Country = namedtuple('Country', ['name', 'capital', 'population'])

country1 = Country(name='France', capital='Paris', population=67000000)
country2 = Country(name='Germany', capital='Berlin', population=83000000)
country3 = Country(name='Italy', capital='Rome', population=59500000)

def country_coll(*args):
    for country in args:
        print(
            f"Country: {country.name}, Capital: {country.capital}, Population: {country.population / 10 ** 6:.1f} mln")

# country_coll(country1, country2, country3)
# Country: France, Capital: Paris, Population: 67.0 mln
# Country: Germany, Capital: Berlin, Population: 83.0 mln
# Country: Italy, Capital: Rome, Population: 59.5 mln

"""Выполнить сериализацию / десериализацию объекта:
person = {"name": "John", "age": 25}

Убедиться в том, словари до преобразования идентичен словарю после.
"""

person_source = {"name": "John", "age": 25}
print(type(person_source))  # dict

person_source_str = json.dumps(person_source)
print(type(person_source_str))  # str

person_destination = json.loads(person_source_str)
print(type(person_destination))  # dict

print(person_source == person_destination)