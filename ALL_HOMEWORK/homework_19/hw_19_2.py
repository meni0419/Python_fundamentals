"""
Напишите функцию is_subset, которая принимает два множества set1 и set2 и проверяет, является ли set1 подмножеством set2. 
Функция должна возвращать True, если все элементы из set1 содержатся в set2, и False в противном случае. 
Функция должна быть реализована без использования встроенных методов issubset или <=.

Пример множеств
{1, 2, 3}
{1, 2, 3, 4, 5}
Пример вывода:
True"""


def is_subset(set1, set2) -> bool:
    return all(item in set2 for item in set1)

def is_subset_v2(set1, set2) -> bool | None:
    for item in set1:
            if item in set2:
                return True
            else:
                return False


set_1 = {1, 2, 3}
set_2 = {1, 2, 3, 4, 5}
print(f"Является ли {set_1} подмножеством {set_2}? (v1) {is_subset(set_1, set_2)}")
print(f"Является ли {set_1} подмножеством {set_2}? (v2) {is_subset(set_1, set_2)}")
print(f"Является ли {set_1} подмножеством {set_2}? (v3) {set_1 <= set_2}")
print(f"Является ли {set_1} подмножеством {set_2}? (v4) {set_1.issubset(set_2)}")
