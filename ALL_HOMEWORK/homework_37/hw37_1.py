"""
В базе данных ich_edit три таблицы. Users с полями (id, name, age), Products с полями (pid, prod, quantity) и Sales с полями (sid, id, pid).

Программа должна запросить у пользователя название таблицы и вывести все ее строки или сообщение, что такой таблицы нет.
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

try:
    with mysql.connector.connect(**dbconfig) as connection:
        with connection.cursor() as cursor:
            table_name = input("Please enter the table name: ")
            cursor.execute(f"SELECT * FROM {table_name}")
            result = cursor.fetchall()
            if result:
                print(f" ===== Table '{table_name}': =====")
                print(result)
            else:
                print(f"table {table_name} does not exist!")
except mysql.connector.Error as err:
    print(f"Something went wrong: {err}")