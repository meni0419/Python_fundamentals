"""5. Напишите функцию, которая вернет количество четных чисел в данном массиве.
"""


def count_in_array(array):
    for i in array:
        if i % 2 != 0:
            array.remove(i)
    return len(array)


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(count_in_array(array))

"""подсмотрел, не понимаю:
def count_in_array(array):
    return len([x for x in array if x % 2 == 0])

x это же один элемент итерации цикла как оно может собираться в кучу значений? 
Скрытый/встроенный append(x) потому что "x for x" конструкция?
"""
