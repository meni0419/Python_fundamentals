"""Сложение ДНК-цепочек"

Создайте класс DNA, представляющий цепочку ДНК (строку из букв A, T, C, G).
При сложении двух цепочек должна получаться новая рекомбинированная цепь —
попеременное чередование нуклеотидов из обеих цепей.

При одинаковой длине ДНК происходит попарное сложение нуклеотидов.
Если цепочки разной длины, то разница добавляется в конец цепочки-результата

Пример:

dna1 = DNA("ATCG")
dna2 = DNA("GCTA")

dna3 = dna1 + dna2
print(dna3)  # DNA("AGTCCGTA")

dna3 = DNA("ATCGA")
dna4 = DNA("GC")

print(dna3 + dna4)  # DNA("AGTCCGA")
dna5 = DNA("AT")
dna6 = DNA("GCTA")

print(dna5 + dna6) # DNA("AGTCTA")
print(dna5 + 5) # TypeError: unsupported operand type(s) for +: 'DNA' and 'int'
"""
from itertools import zip_longest


class DNA:
    def __init__(self, sequence):
        self.sequence = sequence  # последовательность

    def __add__(self, other):
        return DNA(''.join(n1 + n2 for n1, n2 in zip_longest(self.sequence, other.sequence, fillvalue='')))

    # def __add__(self, other):
    #     result = ''
    #     for n1, n2 in zip_longest(self.sequence, other.sequence, fillvalue=''):
    #         result += n1 + n2
    #     return DNA(result)


    def __str__(self):
        return f"DNA({self.sequence})"  # возвращает текстом результат


dna1 = DNA("ATCG")
dna2 = DNA("GCTA")
print(dna1 + dna2)  # DNA("AGTCCGTA")

dna3 = DNA("ATCGA")
dna4 = DNA("GC")
print(dna3 + dna4)  # DNA("AGTCCGA")

dna5 = DNA("AT")
dna6 = DNA("GCTA")
print(dna5 + dna6)  # DNA("AGTCTA")

try:
    print(dna5 + 5)  # TypeError: unsupported operand type(s) for +: 'DNA' and 'int'
except Exception as e:
    print(f'{e.__class__.__name__}: {e}')

# DNA("AGTCCTGA")
# DNA("AGTCCGA")
# DNA("AGTCTA")
# TypeError: unsupported operand type(s) for +: 'DNA' and 'int'
