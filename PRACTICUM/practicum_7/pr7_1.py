"""1. Дан массив целых чисел. Написать функцию, которая вернет true, если 6 является первым или
последним элементом массива, false в противном случае. Массив минимальной длины 1. """


def check_6(array):
    return 6 in array[:1] or 6 in array[-1:]


print(check_6([1, 2, 3, 4, 5, 6]))


def check_6_v2(array):
    return 6 == array[0] or 6 == array[-1]


print(check_6_v2([1, 2, 3, 4, 5, 6]))
