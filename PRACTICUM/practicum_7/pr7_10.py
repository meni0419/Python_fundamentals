"""
10. Дан список, упорядоченный по не убыванию элементов в нем. Определите, сколько в нем
различных элементов. {1, 2, 2, 3, 3, 3} -> 3, {1 1 1 1 1} -> 1
"""


def count_unique_p7_10(array):
    unique_elements = []
    for item in array:
        if item not in unique_elements:
            unique_elements.append(item)
    return len(unique_elements)


array = [1, 2, 2, 3, 3, 3]
print(count_unique_p7_10(array))

"""
сам не догадался:
def count_unique_p7_10(array):
    return len(set(array))

array = [1, 2, 2, 3, 3, 3]
print(count_unique_p7_10(array))"""
