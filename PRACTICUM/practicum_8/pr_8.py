"""1. Дано предложение из слов, разделенных пробелами.
Написать функцию transform(), которая принимает такое предложение и возвращает аналогичное,
но где все слова длины 3 в этом предложении - заглавными буквами.

Пример:
“The quick brown fox jumps over the lazy dog” -> “THE quick brown FOX jumps over THE lazy DOG”.
"""

def transform(text: str) -> str:
    text = text.split()
    result = ""
    for word in text:
        if len(word) == 3:
            result += word.upper() + " "
        else:
            result += word + " "
    return result


sentence = "The quick brown fox jumps over the lazy dog"
result = transform(sentence)
print(result)   # THE quick brown FOX jumps over THE lazy DOG