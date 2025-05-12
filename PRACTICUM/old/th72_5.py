"""БД и запросы на изменение"""

# Подключение библиотеки, соответствующей типу требуемой базы данных
import pysqlite3

connection = pysqlite3.connect("demo.sqlite")
cursor = connection.cursor()


try:
    # ---------------------------Запрос на изменение----------------------------- #
    cursor.executemany(
        "INSERT INTO Artist VALUES (?, ?)",
        [(None, 'No_name_1'), (None, 'No_name_2'), (None, 'No_name_3')]
    )
    connection.commit()

    cursor.execute("SELECT COUNT(*) FROM Artist")
    result = cursor.fetchone()
    print(*result)

    cursor.execute("SELECT COUNT(*) FROM Artist")
    result = cursor.fetchone()[0]
    print(result)



except Exception as e:
    connection.rollback()
    print(e)

finally:
    cursor.close()
    connection.close()




