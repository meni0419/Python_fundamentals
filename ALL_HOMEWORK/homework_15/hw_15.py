# ANSI escape codes for text colors
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"  # Resets the text color to default

print(
    f"""{BLUE}1. Напишите функцию, которая принимает список кортежей от пользователя, где каждый кортеж содержит 
информацию о студенте (имя, возраст, средний балл). Программа должна вывести на экран имена студентов, 
чей средний балл выше заданного значения. Используйте методы кортежей и циклы для обработки данных.
Выведите итоговый список на экран с помощью команды print.

Пример списка кортежей:
{GREEN}[("Alice", 20, 90), ("Bob", 19, 80), ("Charlie", 21, 95), ("David", 18, 85)]{RESET}
{BLUE}Пример вывода:
{GREEN}Введите пороговое значение среднего балла: 90
Студенты с средним баллом выше 90 : ['Charlie']\n{RESET}""")


def average_grades(students, average_grade):
    students_list = []
    for student in students:
        if student[2] > average_grade:
            students_list += [student[0]]
    print(f"Студенты с средним баллом выше {average_grade}: "
          f"{GREEN}{students_list}{RESET}")


students = [("Alice", 20, 90), ("Bob", 19, 80), ("Charlie", 21, 95), ("David", 18, 85)]


def check_grades():
    try:
        grade_count = int(input("Введите пороговое значение среднего балла: "))
        average_grades(students, grade_count)
    except ValueError:
        print(f"{RED}err: there is wrong count{RESET}")
        check_grades()


check_grades()

print(
    f"""{BLUE}\n2. Напишите программу, которая принимает строку от пользователя и разбивает ее на отдельные слова. 
Затем программа должна создать новый кортеж, содержащий длину каждого слова в исходной строке. 
Используйте методы строк и кортежей для обработки данных.

Пример вывода:
{BLUE}Введите предложение: {GREEN}Программирование это интересно и полезно
{BLUE}Длины слов в предложении: {GREEN}(15, 3, 8, 2, 6) {RED}err: there is wrong count{RESET}""")


def word_lengths():
    string = input("Введите предложение: ")
    words_cortege = tuple(string.split())
    words_length = []
    for word in words_cortege:
        words_length.append(len(word))
    words_length = tuple(words_length)
    print(f"Длины слов в предложении:{GREEN}{words_length}{RESET}")


word_lengths()
