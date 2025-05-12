import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv('../../.env')

dbconfig = {
    'host': os.getenv('LOCAL_HOST'),
    'user': os.getenv('LOCAL_USER'),
    'password': os.getenv('LOCAL_PASSWORD'),
    'database': 'ICH_Practicum',
}

with mysql.connector.connect(**dbconfig) as connection:
    with connection.cursor() as cursor:

        cursor.executemany(
            "INSERT INTO Artist (Artist, age) VALUES (%s, %s)",
            [('No_name_1', 50), ('No_name_2', 30), ('No_name_3', 25)]
        )
        connection.commit()

        cursor.execute(
            "SELECT * FROM Artist"
        )
        result = cursor.fetchall()
        print(result)



