""" =============================================================================================
2. Изменим условие 1 задачи:
нужно, чтобы функция из примера 1 могла также менять слова длины 4 на написанные маленькими буквами.
В общем виде, нужно, чтобы функции можно было дать условие, которому соответствует указанное действие.

Например, все слова длины 4 хотим заменить на звёздочки.
А слова длины 2 - на чёрточки.
Каждое выполнение функции - одно условие и одно действие.
"""


def transform(n_law: list, text: str = "") -> str:
    words = text.split()
    for length, func in n_law:
        words = [func(word) if len(word) == length else word for word in words]
    return ' '.join(words)

def transform_2(n_law: list, text: str = "") -> str:
    words = text.split()
    t_words = []
    for word in words:
        t_word = word
        for length, func in n_law:
            if len(word) == length:
                t_word = func(word)
        t_words.append(t_word)
    return ' '.join(t_words)


sentence = "The quick brown Fox jumps Over the Lazy dog"
result = transform_2(
    [
        (3, lambda word: word.upper()),
        (4, lambda word: '_'.join(list(word)).lower()),
        (5, lambda word: '*****')
    ], text=sentence
)
print(result)  # THE quick brown F_o_x jumps Over THE Lazy dog
