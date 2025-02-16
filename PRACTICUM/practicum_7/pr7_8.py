"""
8. Поменяйте предыдущую задачу так, чтобы функция возвращала true если в массиве стоят
рядом два любых одинаковых элемента.
"""


def two_elements(array):
    for i in range(len(array) - 1):
        if array[i] == array[i + 1]:
            return True
    return False


array = [1, 2, 3, 2, 2, 5, 5, 1]
print(two_elements(array))
