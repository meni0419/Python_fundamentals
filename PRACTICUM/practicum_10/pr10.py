"""Словарь синонимов.
Вам дан словарь, состоящий из пар слов.
Каждое слово является синонимом к парному ему слову.
Все слова в словаре различны.
Написать функцию, которая для заданного слова из словаря, определяет его синоним.

Пример словаря:
    dct = {"Hello": "Hi", "Bye": "Goodbye", "List": "Array"}

    get_synonym(“Goodbye”) -> Bye.
    get_synonym(“Plate) -> THe word <Plate> was not found in the dictionary!
"""


def get_synonym(synonyms: dict, word: str) -> str:
    for key, value in synonyms.items():
        if word.lower() in key.lower():
            return value
        elif word.lower() in value.lower():
            return key
        else:
            continue
    return f"Word <{word}> was not found in the dictionary!"

words = {"Hello": "Hi", "Bye": "Goodbye", "List": "Array"}

print(get_synonym(words, "Goodbye"))  # Bye
print(get_synonym(words, "List"))  # Array
print(get_synonym(words, "Plate"))  # Word <Plate> was not found in the dictionary!
