"""Дополните условие предыдущей задачи:
Информацию о продажах необходимо вывести в файл 'sales-by-customers.json'
"""
import json


def read_list_from_json_file(filename: str) -> list:
    sales_list = []
    with open(filename) as file:
        file = json.load(file)
        for i in file:
            sales_list.append(i.split('-'))
    return sales_list


def process_sales_data(file_in: str, file_out) -> None:
    sales = read_list_from_json_file(file_in)
    sales_dictionary = {}
    for customer, item, cnt in sales:
        sales_dictionary[customer] = {}
        if item in sales_dictionary:
            sales_dictionary[customer][item] += cnt
        else:
            sales_dictionary[customer][item] = cnt
    write_list_from_json_file(file_out, sales_dictionary)
    print('Done')


def write_list_from_json_file(filename: str, dct: dict[str, dict[str, int]]) -> None:
    with open(filename, 'w') as file:
        json.dump(dct, file)



process_sales_data('sales.json', 'sales-by-customers.json')
