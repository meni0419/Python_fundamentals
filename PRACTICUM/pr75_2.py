"""
Подключиться к БД sakila на сервере ich-edit

Реализовать сценарий, в которам пользователю предлагается найти фильмы,
в названии которые есть указанное пользователем ключевое слово.

Если фильмов окажется более 10,
выводит их на экран по 10, каждый раз спрашивая пользователя "Продолжить вывод?"

Если ничего найти не удалось - вывести соответствующее сообщение.
"""

import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv('../.env')

dbconfig = {
    'host': os.getenv('ICH_EDIT_HOST'),
    'user': os.getenv('ICH_EDIT_USER'),
    'password': os.getenv('ICH_EDIT_PASSWORD'),
    'database': 'sakila',
}

while True:
    search_req = input("Enter film or actor or genre or year or year and genres (or 'exit' to quit): ").lower()

    if search_req == 'exit':
        print("Exiting program...")
        break
    elif search_req == 'film':
        keyword_film = input("Enter keyword to search in film titles: ")
        break
    elif search_req == 'actor':
        keyword_actor = input("Enter keyword to search in actor names: ")
        break
    elif search_req == 'genre':
        keyword_genre = input("Enter keyword to search in genre: ")
        break
    elif search_req == 'year':
        keyword_year = input("Enter keyword to search in year like =1989 or between 1989 AND 1999: ")
        break
    elif search_req == 'year and genres':
        keyword_genre = input("Enter keyword genres to search in genre: ")
        keyword_year = input("Enter keyword year to search in year like =1989 or between 1989 AND 1999: ")
        break
    else:
        print("Invalid input. Please enter 'film', 'actor' or 'exit'.")

try:
    with mysql.connector.connect(**dbconfig) as connection:
        with connection.cursor() as cursor:
            if search_req == 'film':
                cursor.execute("SELECT title, description FROM film WHERE title LIKE %s", (f"%{keyword_film}%",))
            elif search_req == 'actor':
                cursor.execute(
                    "SELECT title, description, CONCAT(first_name, ' ', last_name) FROM actor, film_actor, film WHERE CONCAT(first_name, ' ', last_name) LIKE %s AND film_actor.film_id = film.film_id AND film_actor.actor_id = actor.actor_id",
                    (f"%{keyword_actor.upper()}%",))
            elif search_req == 'genre':
                cursor.execute(
                    "SELECT title, description, category.name FROM film, film_category, category WHERE category.name LIKE %s AND film_category.film_id = film.film_id AND film_category.category_id = category.category_id",
                    (f"%{keyword_genre}%",))
            elif search_req == 'year':
                cursor.execute(
                    f"SELECT title, description, release_year FROM film WHERE release_year {keyword_year}"
                )
            elif search_req == 'year and genres':
                cursor.execute(
                    "SELECT title, description, category.name, release_year FROM film, film_category, category WHERE release_year {keyword_year} AND {keyword_genre}",
                    (f"%{keyword_year}%,{keyword_year}"))

            results = cursor.fetchall()

            if not results:
                print(f"No films found with the given keyword.")
            else:
                total_pages = len(results)
                start = 0
                page_size = 10

                while start < total_pages:
                    end = min(start + page_size, total_pages)
                    for row in results[start:end]:
                        print(
                            f"\033[1;32mTitle:\033[0m {row[0]}\n\033[1;32mDescription:\033[0m {row[1]}\n \033[1;32m{search_req} :\033[0m {row[2]}")

                    start = end
                    if start < total_pages:
                        cont = input("Continue output? (y/n): ")
                        if cont.lower() != 'y':
                            break

except mysql.connector.Error as err:
    print(f"Database error: {err}")
