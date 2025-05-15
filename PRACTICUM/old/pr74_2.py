"""
В базе данных ich_edit три таблицы. Users с полями (id, name, age), Products с полями (pid, prod, quantity) и Sales с полями (sid, id, pid). Написать мини-интерфейс к базе данных, который умеет выполнять разные команды.
Выбрать таблицу для запроса.

1.) Предусмотреть возможность выбрать несколько таблиц. Вывести результат их соединения, если это возможно, или сообщение об ошибке.
2.) Выбрать одно поле из выбранной таблицы и искомое значение этого поля. Вывести все подходящие строки
"""

import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv('../../.env')

dbconfig = {
    'host': os.getenv('ICH_EDIT_HOST'),
    'user': os.getenv('ICH_EDIT_USER'),
    'password': os.getenv('ICH_EDIT_PASSWORD'),
    'database': 'ich_edit',
}


def prepare_query(tables):
    tables = [t.strip() for t in tables.split(',')]

    if len(tables) > 1:
        join_map = {
            ('Users', 'Sales'): 'Users.id = Sales.id',
            ('Sales', 'Users'): 'Users.id = Sales.id',
            ('Sales', 'Products'): 'Sales.pid = Products.pid',
            ('Products', 'Sales'): 'Sales.pid = Products.pid'
        }

        query = f"SELECT * FROM {tables[0]}"
        all_can_be_joined = True

        for i in range(1, len(tables)):
            pair = (tables[i - 1], tables[i])
            if pair not in join_map:
                all_can_be_joined = False
                break

            join_condition = join_map[pair]
            query += f" JOIN {tables[i]} ON {join_condition}"

        if not all_can_be_joined:
            return "ERROR: Tables cannot be joined"

        search = input("\nDo you want to search by field value? (y/n): ")
        if search.lower() == 'y':
            field = input("Enter field name: ")
            value = input("Enter search value: ")
            query += f" WHERE {field} = '{value}'"

        return query
    else:
        table = tables[0]
        print(f"\nAvailable fields in {table}:")
        field_maps = {
            'Users': ['id', 'name', 'age'],
            'Products': ['pid', 'prod', 'quantity'],
            'Sales': ['sid', 'id', 'pid']
        }
        print(field_maps.get(table, []))

        search = input("\nDo you want to search by field value? (y/n): ")
        if search.lower() == 'y':
            field = input("Enter field name: ")
            value = input("Enter search value: ")
            return f"SELECT * FROM {table} WHERE {field} = '{value}'"
        return f"SELECT * FROM {table}"


print("\nAvailable tables: Users, Sales, Products")
input_tables = input("Enter tables (comma-separated): ")

prepared_query = prepare_query(input_tables)
print(f"\nExecuting query: {prepared_query}")

if not prepared_query.startswith("ERROR"):
    with mysql.connector.connect(**dbconfig) as connection:
        with connection.cursor() as cursor:
            cursor.execute(prepared_query)
            result = cursor.fetchall()
            print("\nResults:")
            for row in result:
                print(row)
else:
    print(prepared_query)
