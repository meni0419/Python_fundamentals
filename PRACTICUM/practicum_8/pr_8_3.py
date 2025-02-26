""" =============================================================================================
3. Подумайте, как уменьшить количество кода в решении задачи 2, например,
избавившись от явных циклов и использовать python comprehension вместо них.
"""


def transform(n_law: list, text: str = "") -> str:
    words = text.split()
    for length, func in n_law:
        words = [func(word) if len(word) == length else word for word in words ]
    return ' '.join(words)


sentence = "The quick brown Fox jumps Over the Lazy dog"
result = transform(
    [
        (3, lambda word: word.upper()),
        (4, lambda word: '_'.join(list(word)).lower()),
        (5, lambda word: '*****')
    ], text=sentence
)
print(result)  # THE quick brown F_o_x jumps Over THE Lazy dog
