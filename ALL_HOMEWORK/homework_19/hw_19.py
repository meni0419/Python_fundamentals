"""
Напишите программу, которая принимает список слов и возвращает список, содержащий только анаграммы.
Анаграммы - это слова, составленные из одних и тех же букв, но в разном порядке.
Создайте функцию anagrams, которая принимает список слов в качестве аргумента и возвращает список анаграмм.
Используйте множества и сортировку букв в слове для проверки на анаграмму. Выведите результат на экран.

Пример переданного списка слов:
['cat', 'dog', 'tac', 'god', 'act']
Пример вывода:
Анаграммы: ['dog', 'god'], ['cat', 'tac', 'act']"""


def anagrams_v1(words):
    words_copy = words.copy()
    anagrams_str = []
    for word in words:
        anagram_list = []
        for word2 in words_copy:
            if set(word) == set(word2):
                anagram_list.append(word2)
                words.remove(word2)
        anagrams_str.append(anagram_list)
    return anagrams_str


words = ['cat', 'dog', 'tac', 'god', 'act']
print(f"Анаграммы (v1): {', '.join(str(group) for group in anagrams_v1(words) if len(group) > 1)}")


def anagrams_v2(words):
    # Создаем словарь для группировки анаграмм
    anagram_dict = {}

    # Проходим по каждому слову в списке
    for word in words:
        # Сортируем буквы в слове и используем их как ключ
        sorted_word = ''.join(sorted(word))

        # Если ключ уже есть в словаре, добавляем слово в список анаграмм
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        # Иначе создаем новую запись в словаре
        else:
            anagram_dict[sorted_word] = [word]

    # Возвращаем только те списки, где больше одного слова (анаграммы)
    return [group for group in anagram_dict.values() if len(group) > 1]


words = ['cat', 'dog', 'tac', 'god', 'act']
print("Анаграммы (v2):", ', '.join(str(group) for group in anagrams_v2(words)))

"""
Напишите функцию is_subset, которая принимает два множества set1 и set2 и проверяет, является ли set1 подмножеством set2. 
Функция должна возвращать True, если все элементы из set1 содержатся в set2, и False в противном случае. 
Функция должна быть реализована без использования встроенных методов issubset или <=.

Пример множеств
{1, 2, 3}
{1, 2, 3, 4, 5}
Пример вывода:
True"""


def is_subset(set1, set2):
    for item in set1:
        if item in set2:
            return True
        else:
            return False


set_1 = {1, 2, 3}
set_2 = {1, 2, 3, 4, 5}
print(f"Является ли {set_1} подмножеством {set_2}? (v1) {is_subset(set_1, set_2)}")
print(f"Является ли {set_1} подмножеством {set_2}? (v2) {set_1 <= set_2}")
print(f"Является ли {set_1} подмножеством {set_2}? (v3) {set_1.issubset(set_2)}")
