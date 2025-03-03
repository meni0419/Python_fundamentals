"""
Напишите программу, которая принимает список слов и возвращает список, содержащий только анаграммы.
Анаграммы - это слова, составленные из одних и тех же букв, но в разном порядке.
Создайте функцию anagrams, которая принимает список слов в качестве аргумента и возвращает список анаграмм.
Используйте множества и сортировку букв в слове для проверки на анаграмму. Выведите результат на экран.

Пример переданного списка слов:
['cat', 'dog', 'tac', 'god', 'act']
Пример вывода:
Анаграммы: ['dog', 'god'], ['cat', 'tac', 'act']"""


def anagrams(words):
    anagrams_str = []
    for word in words:
        anagrams_list = [word]
        for word2 in words:
            if set(word) == set(word2) and word != word2:
                anagrams_list.append(word2)
                words.remove(word2)
        anagrams_str.append(anagrams_list)
    return anagrams_str


words = ['cat', 'dog', 'tac', 'god', 'act']
print("Анаграммы:", ', '.join(str(group) for group in anagrams(words)))  # Анаграммы: ['dog', 'god'], ['cat', 'tac', 'act']"""

"""попытки решить по другому"""


# снова словарь)
def anagrams_base(words):
    anagram_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_dict.setdefault(sorted_word, []).append(word)

    # Возвращаем значения словаря (только те, где больше одного слова)
    return [group for group in anagram_dict.values()]


# вариант сравнивать по сету
def anagrams_v1_0(words):
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


# словарь и через сортировку
def anagrams_v1_1(words):
    # Создаем копию исходного списка для работы
    words_copy = words.copy()
    anagrams_str = []

    while words_copy:  # Пока есть слова в words_copy
        word = words_copy.pop(0)  # Извлекаем первое слово
        anagram_list = [word]  # Оно точно является анаграммой самому себе
        # Проходим по оставшимся словам, чтобы найти анаграммы
        words_to_remove = []
        for word2 in words_copy:
            # Слова являются анаграммами, если отсортированные символы совпадают
            if sorted(word) == sorted(word2):
                anagram_list.append(word2)
                words_to_remove.append(word2)
        # Удаляем найденные анаграммы из words_copy
        for word2 in words_to_remove:
            words_copy.remove(word2)
        # Добавляем список анаграмм в итоговый список
        anagrams_str.append(anagram_list)

    return anagrams_str


# словарь и немного другое использование сортировки
def anagrams_v2_0(words):
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
print("===попытки решить по другому===")
print("Анаграммы (base):", ', '.join(str(group) for group in anagrams_base(words)))
print("Анаграммы (v2_0):", ', '.join(str(group) for group in anagrams_v2_0(words)))
print("Анаграммы (v1_1):", ', '.join(str(group) for group in anagrams_v1_1(words) if len(group) > 1))
print("Анаграммы (v1_0):", ', '.join(str(group) for group in anagrams_v1_0(words) if len(group) > 1))
