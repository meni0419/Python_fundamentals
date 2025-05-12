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

with mysql.connector.connect(**dbconfig) as connection:
    with connection.cursor() as cursor:

        # Получение списка таблиц
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()

        # Вывод списка таблиц
        print("Список таблиц в базе данных:")
        for table in tables:
            print(table[0])



