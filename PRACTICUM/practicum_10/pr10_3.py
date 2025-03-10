"""Дана база данных о продажах некоторого интернет-магазина.
Каждая строка файла 'sales.json' представляет собой запись вида
покупатель-товар-количество, где
    покупатель — имя покупателя (строка без пробелов),
    товар — название товара (строка без пробелов),
    количество — количество приобретенных единиц товара.

Создайте список всех покупателей, а для каждого покупателя подсчитайте количество приобретенных
им единиц каждого вида товаров.
Список покупателей, а также список товаров для каждого покупателя
нужно выводить в лексикографическом порядке.

Данные:
[
    "Alice-apple-5",
    "Alice-orange-3",
    "Bob-apple-2",
    "Bob-banana-7",
    "Alice-banana-2",
    "Charlie-apple-1
]

Пример вывода:
    {'Alice': {'apple': 5, 'banana': 2, 'orange': 3},
     'Bob': {'apple': 2, 'banana': 7},
     'Charlie': {'apple': 1}}
"""
import json
from pprint import pprint


def read_list_from_json_file(filename: str) -> list:
    sales_list = []
    with open(filename) as file:
        file = json.load(file)
        for i in file:
            sales_list.append(i.split('-'))
    return sales_list


# print(read_list_from_json_file("sales.json"))

def process_sales_data(filename: str) -> dict[str, dict[str, int]]:
    sales = read_list_from_json_file(filename)
    sales_dictionary = {}
    for customer, item, cnt in sales:
        if customer not in sales_dictionary:
            sales_dictionary[customer] = {}
        if item in sales_dictionary:
            sales_dictionary[customer][item] += cnt
        else:
            sales_dictionary[customer][item] = cnt
    return sales_dictionary


sales_dict = process_sales_data('sales.json')
pprint(sales_dict)

# {'Alice': {'apple': 5, 'banana': 2, 'orange': 3},
#  'Bob': {'apple': 2, 'banana': 7},
#  'Charlie': {'apple': 1}}
