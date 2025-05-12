"""
Доработать мини-интерфейс к базе данных, который был сделан на занятии. Новые возможности интерфейса:
1. Ввести список полей выбранной таблицы.
2. При вводе искомого значения добавить возможность выбора знака - найти записи, в которых выбранное поле больше, меньше или равно введенному значению.
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

FIELD_MAPS = {
    'Users': ['id', 'name', 'age'],
    'Products': ['pid', 'prod', 'quantity'],
    'Sales': ['sid', 'id', 'pid']
}

JOIN_MAP = {
    ('Users', 'Sales'): 'Users.id = Sales.id',
    ('Sales', 'Users'): 'Users.id = Sales.id',
    ('Sales', 'Products'): 'Sales.pid = Products.pid',
    ('Products', 'Sales'): 'Sales.pid = Products.pid'
}


def display_available_fields(tables):
    print("\nAvailable fields:")
    for table in tables:
        print(f"{table}: {FIELD_MAPS.get(table, [])}")


def get_fields_input():
    return input("\nWhat fields need to display?\n"
                 "Enter fields '*' for all\n"
                 "or comma-separated e.g. Users.id: ")


def build_join_clause(tables):
    join_clauses = []
    for i in range(1, len(tables)):
        prev_table = tables[i - 1]
        curr_table = tables[i]
        join_condition = JOIN_MAP.get((prev_table, curr_table))

        if not join_condition:
            return None, "ERROR: Tables cannot be joined"

        join_clauses.append(f" JOIN {curr_table} ON {join_condition}")
    return ''.join(join_clauses), None


def get_search_condition():
    search = input("\nDo you want to search by field value? (y/n): ")
    if search.lower() != 'y':
        return None

    field = input("Enter field name e.g. Users.id: ")
    value = input("Enter search value e.g. >30 or ='Bob': ")
    return f"{field} {value}"


def prepare_query(tables_str):
    tables = [t.strip() for t in tables_str.split(',')]

    for table in tables:
        if table not in FIELD_MAPS:
            return f"ERROR: Table '{table}' doesn't exist"

    display_available_fields(tables)
    fields = get_fields_input()

    if len(tables) == 1:
        query = f"SELECT {fields} FROM {tables[0]}"
    else:
        join_clause, error = build_join_clause(tables)
        if error:
            return error
        query = f"SELECT {fields} FROM {tables[0]}{join_clause}"

    # Add search condition
    search_condition = get_search_condition()
    if search_condition:
        query += f" WHERE {search_condition}"

    return query


print("\nAvailable tables: Users, Sales, Products")
input_tables = input("Enter tables (comma-separated): ")

prepared_query = prepare_query(input_tables)

if not prepared_query.startswith("ERROR"):
    try:
        print(f"\nExecuting query:\n {prepared_query}")
        with mysql.connector.connect(**dbconfig) as connection:
            with connection.cursor() as cursor:
                cursor.execute(prepared_query)
                result = cursor.fetchall()
                print("\nResults:")
                for row in result:
                    print(row)
    except mysql.connector.Error as err:
        print(f"\nDatabase error: {err}")
else:
    print(prepared_query)
