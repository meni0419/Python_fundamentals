"""В базе данных ich_edit три таблицы:
    Users с полями (id, name, age),
    Products с полями (pid, prod, quantity) и
    Sales с полями (sid, id, pid).

Дан список с именами таблиц.
Программа должна в цикле сделать запрос к каждой из указанных таблиц.
Если таблица есть в базе - вывести на печать её содержимое.
Если нет - вывести сообщение:"The table {table_name} does not exist!"
"""


import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv('../.env')

dbconfig = {
    'host': os.getenv('ICH_EDIT_HOST'),
    'user': os.getenv('ICH_EDIT_USER'),
    'password': os.getenv('ICH_EDIT_PASSWORD'),
    'database': 'ich_edit',
}

list_tables = ['Users', 'Products', 'Sales']

with mysql.connector.connect(**dbconfig) as connection:
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES;")
        exist_tables = cursor.fetchall()
        exist_tables = [table[0] for table in exist_tables]
        # print(exist_tables)

        try:
            for table in list_tables:
                if table not in exist_tables:
                    print(f"The table <{table}> does not exist!")
                    continue

                cursor.execute(f"SELECT * FROM {table}")
                result = cursor.fetchall()
                if result:
                    print(f" ===== Table '{table}': =====")
                    print(result)
                else:
                    print(f"table {table} does not exist!")
        except Exception as e:
            print(e)




#  ===== Table 'Users': =====
# (1, 'John Doe', 30)
#  ===== Table 'Products': =====
# (1, 'Laptop', 20)
#  ===== Table 'Sales': =====
# (1, 1, 1)
# Тhe table <No_name> does not exist!
