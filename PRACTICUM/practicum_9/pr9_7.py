"""
7. На входе функция to_set() получает строку или список чисел. Преобразуйте их в множество. На
выходе должно получиться множество и его мощность.
"""

def to_set(seq: list | str) -> tuple[set, int]:
    set_seq = set(seq)
    return set_seq, len(set_seq)

print(to_set([1, 2, 3, 4, 5]))   # ({1, 2, 3, 4, 5}, 5)
print(to_set("cardinality"))   # ({'y', 'r', 'a', 'c', 'i', 't', 'l', 'd', 'n'}, 9)