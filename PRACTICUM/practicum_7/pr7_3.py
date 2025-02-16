"""Дан массив целых чисел длины 3. Написать функцию, которая возвращает массив “повернутый
влево”: {1, 2, 3} -> {2, 3, 1}, {5, 11, 9} -> {11, 9, 5}
"""


def left_p7_3(array):
    return array[1:] + [array[0]]


array = [1, 2, 3]
print(left_p7_3(array))


def left_p7_3_v2(array):
    return [array[1]] + [array[2]] + [array[0]]


print(left_p7_3_v2(array))


def left_p7_3_v3(array):
    left_array = array[1:]
    left_array.extend([array[0]])
    return left_array


print(left_p7_3_v3(array))

"""если принципиально {} то использовать set() и list()"""
