"""Добавьте к условиям задачи 1 возможность добавления пользователем собственных синонимов."""


def get_synonym(synonyms: dict, word: str) -> str:
    for key, value in synonyms.items():
        if word in key:
            return value
        elif word in value:
            return key
        else:
            continue
    return f"Word <{word}> was not found in the dictionary!"


def add_synonym(synonyms: dict, word: str, synonym: str) -> dict:
    synonyms[word] = synonym
    return synonyms


words = {"Hello": "Hi", "Bye": "Goodbye", "List": "Array"}
add_synonym(words, "Goodnight", "Night")

print(get_synonym(words, "Goodbye"))  # Bye
print(get_synonym(words, "List"))  # Array
print(get_synonym(words, "Plate"))  # Word <Plate> was not found in the dictionary!
print(get_synonym(words, "Night"))  # Night
