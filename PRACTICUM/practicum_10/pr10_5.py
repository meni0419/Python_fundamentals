"""Добавьте к условиям задачи 1 возможность добавления пользователем собственных синонимов."""
from pr10 import get_synonym


def add_synonym(synonyms: dict, word: str, synonym: str) -> dict:
    synonyms[word] = synonym
    return synonyms


words = {"Hello": "Hi", "Bye": "Goodbye", "List": "Array"}
add_synonym(words, "Goodnight", "Night")

print("Goodbye :", get_synonym(words, "Goodbye"))  # Bye
print("List :", get_synonym(words, "List"))  # Array
print("Plate :", get_synonym(words, "Plate"))  # Word <Plate> was not found in the dictionary!
print("Night :", get_synonym(words, "Night"))  # Night
