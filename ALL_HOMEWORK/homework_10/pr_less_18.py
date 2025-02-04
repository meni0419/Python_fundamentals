# Используя метод find(), найдите позицию слова Mars в строке:
# Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.

# text = "Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."
# print(text.find("Mars"))


"""
================================== Задача 1 ================================
Приходит текст из 5 строк.
Задача:
 - строка не должна начинаться с пробелов, допустима только табуляция (отступ).
 - сделать так, чтобы все строки начинались с большой буквы;
 - не было подряд несколько пробелов и знаков пунктуации;
Не забывайте, что точка не всегда значит конец предложения! Например, и т.д. и т.п.
"""


def clean_text(text):
    """
    Приходит текст из 5 строк.
    Задача:
     - строка не должна начинаться с пробелов, допустима только табуляция (отступ).
     - сделать так, чтобы все строки начинались с большой буквы;
     - не было подряд несколько пробелов и знаков пунктуации;
    Не забывайте, что точка не всегда значит конец предложения! Например, и т.д. и т.п.
    """

    lines = text.split("\n")  # разбиваем текст на предложения
    i = 0
    while i < len(lines):  # делаем цикл 5 раз т.к. в списке 5 элементов
        line = lines[i].strip().capitalize()  # удаляем лишние пробелы и делаем с большой буквы начало
        j = 0
        while j < len(line) - 1:  # делаем цикл по длине предложения, но -1 т.к. потом делаем замену +1 индекс
            # проверяем повторяется ли следующий символ и в списке ли он у нас на исключение
            if line[j] == line[j + 1] and (line[j] in UNIQ_MARK):
                # имитируем пропуск текущего символа, заменяя предложение частью до него и + частью после
                line = line[:j] + line[j + 1:]
            else:
                j += 1
        lines[i] = line  # пересобираем список с каждой итерацией заменяя предложение
        i += 1
    return "\n".join(lines)  # лепим все в одну строку соединяя элементы списка переносом строки


text = """    \thello,,,, world.    how are you???    
    \t I'm fine, thank   you.     
\tI am fine too!!!     
Do you know what means "и т.д. и т.п."?
   \t   I'm fine. Thank you   for your question!           """

UNIQ_MARK = " ,.:;!?!№;%:?"

print(clean_text(text))

# =============== РЕЗУЛЬТАТ ==================
# 	Hello, world. How are you?
# 	I'm fine, thank you.
# 	I am fine too!
# Do you know what means "и т.д. и т.п."
# 	I'm fine. Thank you for your question!

# t= text.split()
# print(*t)

# t = " ".join(t)
# print(t)

# bearer = 'curl - X GET http://127.0.0.1:8000/employees/ -H \"Authorization: Bearer some_token\"'
#
# cookie = "curl - X GET http://127.0.0.1:8000/employees/ --cookie \"access_token=some_token\""
