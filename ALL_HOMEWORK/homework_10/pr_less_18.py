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


# =============== РЕЗУЛЬТАТ ==================
# 	Hello, world. How are you?
# 	I'm fine, thank you.
# 	I am fine too!
# Do you know what means "и т.д. и т.п."
# 	I'm fine. Thank you for your question!


def clean_text(text):
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].strip().capitalize()
        j = 0
        while j < len(line) - 1:
            if (line[j] == line[j + 1]
                    and (line[j] in UNIQ_MARK
                         or line[j] in PUNCTUATION_MARKS_AND_SPACE)):
                line = line[:j] + line[j + 1:]
            else:
                j += 1

        lines[i] = line
        i += 1
    return "\n".join(lines)


text = """    \thello,,,, world.    how are you???    
    \t I'm fine, thank   you.     
\tI am fine too!!!     
Do you know what means "и т.д. и т.п."?
   \t   I'm fine. Thank you   for your question!           """

UNIQ_MARK = "!№;%:?"
PUNCTUATION_MARKS_AND_SPACE = " ,.:;!?"

print(clean_text(text))

# t= text.split()
# print(*t)

# t = " ".join(t)
# print(t)

# bearer = 'curl - X GET http://127.0.0.1:8000/employees/ -H \"Authorization: Bearer some_token\"'
#
# cookie = "curl - X GET http://127.0.0.1:8000/employees/ --cookie \"access_token=some_token\""
