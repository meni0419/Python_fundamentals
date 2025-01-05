"""
1. Напишите программу, которая запрашивает у пользователя строку и преобразует ее, удаляя все гласные буквы из строки.
Используйте метод replace() для замены гласных букв на пустую строку. Выведите преобразованную строку на экран с помощью
команды print.
"""


def remove_vowels(s):
    vowels = "aeiouy"
    s = s.lower()
    for letter in vowels:
        s = s.replace(letter, "")
    s = s.lstrip()
    return s


"""
2. Напишите программу, которая запрашивает у пользователя строку и определяет, содержит ли она только уникальные символы. 
Если все символы в строке уникальны, выведите соответствующее сообщение на экран. В противном случае выведите сообщение 
о том, какие символы повторяются. Не используйте множества и подобные структуры данных, которые мы пока не изучали, 
для проверки уникальности символов.
"""


def is_unique(s):
    s = s.lower()
    repeat_letters = ""
    for letter in s:
        if s.count(letter) > 1 and letter not in repeat_letters:
            repeat_letters += letter + " and "
    if repeat_letters == "":
        print(f"2. All letters in str is unique")
    else:
        print(f"2. Letters {repeat_letters[:-5]} are repeated")


"""
3. Напишите программу, которая запрашивает у пользователя строку и выравнивает ее по центру с заданной шириной. 
Если строка не может быть выровнена по центру из-за нечетной ширины, она должна быть выровнена смещением вправо. 
Используйте методы center() и rjust() для выравнивания строки.
"""


def align_str(s):
    width = int(input("Enter width: "))
    s = s.lower()
    if len(s) % 2 == 0:
        return s.center(width)
    else:
        return s.rjust(width, " ")


req_s = input("Enter string: ")

# 1
print(f"1. {remove_vowels(req_s)}")
# 2
is_unique(req_s)
# 3
print(f"3. {align_str(req_s)}")
