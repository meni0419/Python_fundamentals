"""  ==================================================================
03  У вас есть текстовый файл names.txt, где каждая строка - имя человека.
Написать программу, которая выводит следующее приветствие:
    “Привет, <имя 1>, <имя 2>,... <имя n> и добро пожаловать!”.
Программу реализовать с помощью генератора и суб-генератора, где
    - суб-генератор возвращает имена из файла,
    - а основной генератор в нужный момент считывает и возвращает значения из суб-генератора.
"""


def gen_read_f():
    pass


def gen_main():
    pass


print(f"{', '.join([x for x in gen_main()])} и добро пожаловать!")
# Привет, Alice, John, Max, Maria и добро пожаловать!



""" ===============================================================


04  Возьмите json файл с предыдущего практикума, с клиентами
(имя, фамилия, дата рождения, номер счета)
и реализуйте генератор, который возвращает строки с информацией о клиентах.
Убедитесь, что после вычитывания всех строк из файла,
файловый ресурс корректно освобождается (использования исключения GeneratorExit и очистку ресурсов).
"""
import json


def gen_clients():
    pass


gen = gen_clients()
for client in gen:
    print(client)
gen.close()

# {'name': '', 'surname': 'Doe', 'birth_date': '2005-03-28', 'iban': 'DE44443333222211110000'}
# {'name': 'John', 'surname': 'Smith', 'birth_date': '2008-10-25', 'iban': 'XE345678901234567890'}
# {'name': 'Michael', 'surname': 'Brown', 'birth_date': '1990-05-15', 'iban': 'DE89370400440532013000'}
# {'name': 'Anna', 'surname': 'Johnson', 'birth_date': '1985-12-07', 'iban': '5511112222333344445555'}
# {'name': 'Emily', 'surname': 'Taylor', 'birth_date': '1999-08-03', 'iban': 'DE9876543210987654321A'}
# {'name': '', 'surname': 'Taylor', 'birth_date': '2020-08-03', 'iban': '1465DE9876543210987654321A'}
# {'name': 'Robert', 'surname': 'Davis', 'birth_date': '1992-04-12', 'iban': 'DE1234567890123456789012'}
