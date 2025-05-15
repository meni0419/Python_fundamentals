"""В базе данных ich_edit три таблицы:
    Users с полями (id, name, age),
    Products с полями (pid, prod, quantity) и
    Sales с полями (sid, id, pid).

Программа должна
 - вывести все имена из таблицы Users,
 - дать пользователю выбрать одно из них
 - и вывести все покупки этого пользователя.

 Если покупок по запрашиваемому пользователю не найдено, то выводим:
    "User {user_name} has no purchases"
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


with mysql.connector.connect(**dbconfig) as connection:
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT name FROM Users")
        print(cursor.fetchall())

        select_user = input("Please enter the username: ")
        cursor.execute("""SELECT u.name, p.prod, p.quantity
                          FROM Users u,
                               Sales s,
                               Products p
                       WHERE u.id = s.id
                       AND p.pid = s.pid AND u.name = %s
                       """,[select_user])
        result = cursor.fetchall()

        print(result)



#  ===== Table 'Users': =====
# (1, 'John Doe', 30)
# Please enter the username: John Doe
#  ===== Purchases of User <John Doe> : =====
# ('John Doe', 'Laptop', 20)




