"""
6. Напишите функцию, которая возвращает сумму элементов массива и возвращает 0, если массив
пустой. Так как число 13 приносит неудачу, функция не должна учитывать число 13 и
последующие за ним числа в массиве. {1, 2, 2, 1} -> 6, {0, 2, 2, 3, 13} -> 7, {1, 2, 13, 2, 1} -> 3
"""


def sum_array_p7_6(array):
    if len(array) == 0:
        return 0
    elif 13 not in array:
        return sum(array)
    else:
        for i in range(len(array)):
            if array[i] == 13:
                return sum(array[:i])


print("Сумма массива [] =", sum_array_p7_6([]))
print("Сумма массива [1, 2, 2, 1] =", sum_array_p7_6([1, 2, 2, 1]))
print("Сумма массива [0, 2, 2, 3, 13] =", sum_array_p7_6([0, 2, 2, 3, 13]))
print("Сумма массива [1, 2, 13, 2, 1] =", sum_array_p7_6([1, 2, 13, 2, 1]))


def sum_array_p7_6_v2(array):
    if len(array) == 0:
        return 0
    elif 13 not in array:
        return sum(array)
    else:
        sum_array = 0
        for i in range(len(array)):
            if array[i] == 13:
                return sum_array
            sum_array += array[i]


print("==========v2===========")
print("Сумма массива [] =", sum_array_p7_6_v2([]))
print("Сумма массива [1, 2, 2, 1] =", sum_array_p7_6_v2([1, 2, 2, 1]))
print("Сумма массива [0, 2, 2, 3, 13] =", sum_array_p7_6_v2([0, 2, 2, 3, 13]))
print("Сумма массива [1, 2, 13, 2, 1] =", sum_array_p7_6_v2([1, 2, 13, 2, 1]))
