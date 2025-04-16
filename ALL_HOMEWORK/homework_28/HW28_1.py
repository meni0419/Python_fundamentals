"""
Напишите программу, которая принимает список слов от пользователя и использует генераторное выражение (comprehension) для создания нового списка, содержащего только те слова, которые начинаются с гласной буквы. Затем программа должна использовать функцию map, чтобы преобразовать каждое слово в верхний регистр. В результате программа должна вывести новый список, содержащий только слова, начинающиеся с гласной буквы и записанные в верхнем регистре."""


def text_transform(text: str) -> list:
    vowels = "aeiou"
    text_split = text.split(", ")
    words = [word for word in text_split if word[0].lower() in vowels]
    transformed_words = list(map(lambda word: word.upper(), words))
    # transformed_words = list(map(str.upper, words))
    return transformed_words


print(text_transform("Aello, World, Allo, Arld, aloha, Hello world"))
