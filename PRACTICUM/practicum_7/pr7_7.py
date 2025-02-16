"""
7. Написать функцию, которая возвращает true, если в массиве две двойки идут подряд. {1, 2, 2} ->
true, {2, 1, 2} -> false
"""


def two_doubles(arr, num):
    for i in arr:
        if arr[i] == num and arr[i + 1] == num:
            return True
    return False


arr = [1, 2, 3, 2, 2, 5, 5, 1]
num = 2
print(two_doubles(arr, num))

""" any() не понятно, подсмотрел:
def two_doubles(arr, num):
    return any(arr[i] == num and arr[i + 1] == num for i in range(len(arr) - 1))
"""
