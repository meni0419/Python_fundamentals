""" ===========================================================
02 Напишите генератор, в который
 - передаются строки разной длины
 и который возвращает строки фиксированной длины 7 символов.

Если длина переданной строки  больше 7 символов,
    то возвращаются первые 7 символов.
Если длина переданной строки меньше 7 символов,
    то недостающие символы присоединяются к строке слева в виде нулей (“abcd” -> “000abcd”).
"""


def gen_7_symbols():
    input_str = None
    while True:
        input_str = (yield input_str.zfill(7)[:7] if input_str else None)


g = gen_7_symbols()
next(g)  # Initialize generator

print(g.send('123456789'))  # 1234567
print(g.send('12345'))  # 0012345
