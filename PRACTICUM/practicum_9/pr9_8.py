"""
8. Предоставлен список натуральных чисел.
Требуется сформировать из них множество.
Если какое-либо число повторяется, то преобразовать его в строку по образцу:
например, если число 4 повторяется 3 раза, то в множестве будет следующая запись:
    - само число 4;
    - строка 44 (второе повторение, т.е. число дублируется в строке);
    - строка 444 (третье повторение, т.е. строка множится на 3).

Реализуйте вывод множества через функцию set_gen().
"""


def set_gen(nums: list[int]) -> set[int | str]:
    nums_set = set()
    counts = {}  # словарь для подсчета повторений элемента

    for num in nums:
        if num in counts:
            # Увеличиваем счётчик и добавляем строку в множество
            counts[num] += 1
            nums_set.add(str(num) * counts[num])
        else:
            # Впервые встреченный элемент добавляем в множество как есть
            counts[num] = 1
            nums_set.add(num)

    return nums_set




print(set_gen([1, 1, 1, 2, 2, 3]))   # {1, 2, 3, '111', '22', '11'}

print(set_gen([1, 1, 1, 2, 2, 3]) == {1, 2, 3, '111', '22', '11'})