from PRACTICUM.practicum_2.exercises import set_bool

"""
Перепишите решение следующей задачи с использованием функции. У нас есть две
логические переменные: isWeekday, isVacation (выходной день и каникулы). Они могут
принимать разные значения, всего 4 комбинации: true - true, true - false, false - false, false -
true. Есть правило: мы можем поспать, если день не рабочий или мы на каникулах.
Напишите программу, которая в зависимости от значений двух переменных печатает,
можем ли мы поспать или нет. То есть для значений isWeekday = False и isVacation = False
программа должна печатать “можете поспать”.
"""


def can_sleep(is_week_day, is_vacation):
    if is_week_day and not is_vacation:
        print("No u can't sleep")
    else:
        print("Yes u can sleep")


is_wd = True
is_vacation = False

can_sleep(is_wd, is_vacation)

# can_sleep(
#     is_wd := set_bool(
#         input("Is weekday? (True/False): ")),
#     is_vacation := set_bool(
#         input("Is vacation? (True/False): "))
# )
