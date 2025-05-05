"""Написать программу, которая использует функции языка для работы
с регулярными выражениями и синтаксис регулярных выражений:
"""

import re

task1 = """1. Определите, содержит ли заданная строка набор данных символов (a-z, A-Z и 0-9)."""


def is_data_string_with_num(string):
    return bool(re.search(r'[a-zA-Z0-9]+', string))


print(f"{task1}\n \033[1;32m{is_data_string_with_num(task1)} \033[0m")

task2 = """2. Определите, содержит ли строка символ 'a', за которым следует ноль или более символов 'b'"""


def is_string_with_a_b(string):
    return bool(re.search(r'[a-z]*b+', string))


print(f"{task2}\n \033[1;32m{is_string_with_a_b(task2)} \033[0m")

task3 = """3. Определите, содержит ли строка символ 'a', за которым следует 1 или более символов 'b'"""


def is_string_with_a_b_1_or_more(string):
    return bool(re.search(r'[a-z]b+', string))


print(f"{task3}\n \033[1;32m{is_string_with_a_b_1_or_more(task3)} \033[0m")

task4 = """4. Определите, содержит ли строка символ 'a', за которым следует 0 или 1 символ 'b'."""


def is_string_with_a_b_0_or_1(string):
    return bool(re.search(r'[a-z]?b', string))


print(f"{task4}\n \033[1;32m{is_string_with_a_b_0_or_1(task4)} \033[0m")

task5 = """5. Определите, содержит ли строка символ z."""


def is_string_with_z(string):
    return bool(re.search(r'[z]', string))


print(f"{task5}\n \033[1;32m{is_string_with_z(task5)} \033[0m")

task6 = """6. Определите, содержит ли строка только буквы, цифры и символ подчеркивания."""


def check_string_content(string):
    return bool(re.search(r'^[a-zA-Z0-9_]+$', string))


print(f"{task6}\n \033[1;32m{check_string_content(task6)} \033[0m")

task7 = """7. Определите, начинается ли строка с заданного числа."""


def starts_with_number(string):
    return bool(re.search(r'^7', string))


print(f"{task7}\n \033[1;32m{starts_with_number(task7)} \033[0m")

task8 = """8. Напишите программу, которая удаляет нули (0) перед цифрами в IP адресе.
    Например, "192.01.001.010"  → "192.1.1.10" """


def clean_ip_address(string):
    return re.sub(r'\b0+(?=\d)', '', string)


print(f"{task8}\n \033[1;32m{clean_ip_address(task8)} \033[0m")

task9 = """9. Определите, содержит ли строка цифры в конце."""


def ends_with_digit(string):
    return bool(re.search(r'\d+$', string))


print(f"{task9}\n \033[1;32m{ends_with_digit(task9)} \033[0m")

task10 = """10. Найдите вхождения и позиции подстроки в строке.
    Пример: строка "Домашние задания, задания в классе, отпускные задания",
    подстрока "задания",
    вывод "задания" на 9:15, "задания" на 18:24, "задания" на 46:52."""


def find_substring_positions():
    string = "Домашние задания, задания в классе, отпускные задания"
    substring = "задания"
    positions = []
    for match in re.finditer(substring, string):
        start, end = match.span()
        positions.append(f'"{substring}" на {start}:{end}')
    return ', '.join(positions)


print(f"{task10}\n \033[1;32m{find_substring_positions()} \033[0m")

task11 = """11. Напишите программу, которая заменяет пробелы подчёркиваниями_и_обратно."""


def replace_spaces(string):
    return re.sub(r'\s+', '_', string)


def replace_underscore(string):
    return re.sub(r'_+', ' ', string)


print(f"{task11}\n \033[1;32m{replace_underscore(task11)} \033[0m")

task12 = """12. Частью URL часто является дата в формате 2016/09/02.
    Например, https://www.somesite.com/news/2024/01/22/article.html.
    Найдите все даты в URL такого вида.
    Вывод может выглядеть так [('2024', '01', '22')]."""


def find_dates_in_url(string):
    # return re.findall(r'(\d{4})/(\d{2})/(\d{2})', string)
    return re.findall(r'\d{4}/\d{2}/\d{2}', string)

print(f"{task12}\n \033[1;32m{find_dates_in_url(task12)} \033[0m")

task13 = """13. Напишите программу, которая конвертирует дату в формате 2025-05-25 в формат 25-05-2025."""


def convert_date_format(string):
    return re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3-\2-\1', string)


print(f"{task13}\n \033[1;32m{convert_date_format("2025-05-25")} \033[0m")

task14 = """14. Напишите программу, которая отделяет и печатает цифры в заданной строке.
    Например, для строки "Ten 10, Twenty 20, Thirty 30" должно быть выведено 10, 20, 30."""


def extract_numbers(string):
    return re.findall(r'\d+', string)


print(f"{task14}\n \033[1;32m{extract_numbers(task14)} \033[0m")

task15 = """15. Напишите программу, которая выводит все слова,
    начинающиеся на букву 'а' и 'е' в аданном едложении."""


def find_words_starting_with(string):
    return re.findall(r'\b[а|е]\w+', string)


print(f"{task15}\n \033[1;32m{find_words_starting_with(task15)} \033[0m")

task16 = """16. Напишите программу, которая печатает цифры и их позиции в заданной строке текста."""


def find_digit_positions(string):
    positions = []
    for match in re.finditer(r'\d+', string):
        positions.append(match.span())
    return positions


print(f"{task16}\n \033[1;32m{find_digit_positions(task16)} \033[0m")

task17 = """17. Напишите программу, которая сокращает Strasse на Str. в заданной строке,
    например, "Flensburger Strasse" → "Flensburger Str."."""


def shorten_strasse(string):
    return re.sub(r'\bStr\w+', 'Str.', string)


print(f"{task17}\n \033[1;32m{shorten_strasse("Flensburger Strasse")} \033[0m")

task18 = """18. Напишите программу, которая заменяет все вхождения пробела, запятой или точки подчеркиванием."""


def replace_punctuation(string):
    return re.sub(r'[\s,.]', '_', string)


print(f"{task18}\n \033[1;32m{replace_punctuation(task18)} \033[0m")

task19 = """19. Напишите программу, которая находит все слова длины 3 в заданном предложении."""


def find_three_letter_words(string):
    return re.findall(r'\b\w{3}\b', string)


print(f"{task19}\n \033[1;32m{find_three_letter_words(task19)} \033[0m")

task20 = """20. Напишите программу, которая находит все слов длины 3, 4 и 5 символов 
    в заданном предложении."""


def find_words_by_length(string):
    return re.findall(r'\b\w{3,5}\b', string)


print(f"{task20}\n \033[1;32m{find_words_by_length(task20)} \033[0m")

task21 = """21. Напишите программу, которая превращает camel-case строку в snake-case строку,
    например, "ПайтонПрограммист" -> "пайтон_программист"."""


def camel_to_snake(string):
    return re.sub(r'(?<!^)(?<![\s,.])(?=[А-ЯA-Z])', '_', string).lower()


print(f"{task21}\n \033[1;32m{camel_to_snake("ПайтонПрограммист, PythonDeveloper")} \033[0m")

task22 = """22. Напишите программу, которая выводит значения между кавычками в строке.
    Например, "Python", "PHP", "Java" -> ['Python', 'PHP', 'Java']."""


def extract_quoted_values(string):
    return re.findall(r'"([^"]+)"', string)


print(f"{task22}\n \033[1;32m{extract_quoted_values(task22)} \033[0m")

task23 = """23. Напишите программу, которая удаляет несколько идущих подряд пробелов из строки,
    заменяя их одним пробелом. "Hello     World" -> "Hello World"."""


def normalize_spaces(string):
    return re.sub(r'\s+', ' ', string)


print(f"{task23}\n \033[1;32m{normalize_spaces("Hello     World")} \033[0m")

task24 = """24. Напишите программу, которая удаляет все пробелы из строки."""


def remove_spaces(string):
    return re.sub(r'\s+', '', string)


print(f"{task24}\n \033[1;32m{remove_spaces(task24)} \033[0m")

task25 = """25. Напишите программу, которая заменяет в тексте все слова "xfactor, foton",
    начинающиеся на 'х' или 'f' на звёздочки."""


def replace_words(string):
    return re.sub(r'\b[x|f]\w+\b', '*****', string, flags=re.IGNORECASE | re.MULTILINE)


print(f"{task25}\n \033[1;32m{replace_words(task25)} \033[0m")
