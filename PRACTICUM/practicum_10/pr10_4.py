"""Дополните условие предыдущей задачи:
Информацию о продажах необходимо вывести в файл 'sales-by-customers.json'
"""
import json
from pr10_3 import process_sales_data


def write_list_from_json_file(file_in, file_out) -> None:
    dct = process_sales_data(file_in)
    with open(file_out, 'w') as file:
        json.dump(dct, file)
    print(f'File {file_out} was created')


write_list_from_json_file('sales.json', 'sales-by-customers.json')
