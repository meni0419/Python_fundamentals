""" 02 ===========================================================================

Дан json-файл 'cities-countries.json', в котором
по ключу <Страна> находится строка с названиями городов, разделённых пробелом.

Напишите функцию, которая:
 - считывает данные из файла;
 - по аргументу ГОРОД возвращает
    - либо название страны
    - либо "not found"

which_country("Novgorod") = Russia
which_country("Mumbai") = Not found

"""
import json


def read_json_file(filename: str) -> dict[str, str]:
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def which_country(city: str) -> str:
    cities = read_json_file("cities-countries.json")
    for country, city_list in cities.items():
        if city in city_list:
            return country
        else:
            continue
    return "Not found"


print(which_country("Novgorod"))  # Russia
print(which_country("Kiev"))  # Ukraine
print(which_country("Mumbai"))  # Not found
