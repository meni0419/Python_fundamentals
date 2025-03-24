"""01 Напишите бесконечный генератор, который возвращает последовательность целых чисел,
где каждое следующее больше предыдущего в 2 раза.
"""


def gen_double_num():
    num = 1
    while True:
        yield num
        num *= 2


g = gen_double_num()
print(g.__next__())  # 1
print(g.__next__())  # 2
print(g.__next__())  # 4
print(g.__next__())  # 8
print(g.__next__())  # 16


