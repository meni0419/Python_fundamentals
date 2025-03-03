""" ===================================================================================================
4. Есть магазин по продаже мороженого. Одна порция стоит 5 евро.
В кассе на момент открытия магазина - 0 евро.
В магазин выстраивается очередь покупателей, у которых есть одна купюра, чтобы оплатить порцию мороженого.

Задача: зная купюры всех покупателей в очереди (конечного размера), понять, получится ли продать мороженое всем
(для этого надо иметь достаточно купюр, чтобы давать сдачу), или не получится.

Существуют купюры следующего номинала: 5, 10, 20, 50 евро.
Напишите функцию, которая принимает список с купюрами покупателей.
Например, если очередь имеет купюры [5, 10, 5, 20], то функция вернет true
(первому покупателю продадут мороженое за 5,
со второго возьмут 10 и дадут сдачу 5,
третьему дадут мороженое за 5,
с четвертого возьмут 20 евро и дадут сдачу 15 купюрами 10 и 5 которые есть в кассе).

Подсказка: кассу можно представить в виде списка, отсортированного по возрастанию.
Когда нужно понять, можно ли дать сдачу, то мы перебираем список кассы и суммируем банкноты в нём.
Если они могут в сумме дать сдачу, то мы их убираем из списка, добавляем банкноту,
которой платили, пересортировываем, и так далее).
"""


def can_sell_icecream1(lst: list[int]) -> bool:
    cash = []
    customers = lst.copy()
    print(lst)
    for banknote in lst:
        if banknote == 5 and 5 in customers:
            cash.append(5)
            customers.remove(5)
        if banknote == 10:
            if 5 in customers + cash:
                (customers if 5 in customers else cash).remove(5)
                cash.append(10)
            else:
                return False
        elif banknote == 20:
            if 5 in customers + cash:
                if 10 in customers + cash:
                    (customers if 10 in customers else cash).remove(10)
                    (customers if 5 in customers else cash).remove(5)
                    cash.append(20)
                elif (cash + customers).count(5) >= 3:
                    cash.append(20)
                    for _ in range(3):
                        (customers if 5 in customers else cash).remove(5)
                else:
                    return False
            else:
                return False
        elif banknote == 50:
            if 5 in customers + cash:
                if (customers + cash).count(20) >= 2:
                    cash.append(50)
                    for _ in range(2):
                        (customers if 20 in customers else cash).remove(20)
                    (customers if 5 in customers else cash).remove(5)
                elif 20 in cash + customers and (cash + customers).count(10) >= 2:
                    cash.append(50)
                    for _ in range(2):
                        (customers if 10 in customers else cash).remove(10)
                    (customers if 20 in customers else cash).remove(20)
                    (customers if 5 in customers else cash).remove(5)
                elif 20 in customers + cash and 10 in customers + cash and (customers + cash).count(5) >= 3:
                    cash.append(50)
                    for _ in range(3):
                        (customers if 5 in customers else cash).remove(5)
                    (customers if 20 in customers else cash).remove(20)
                    (customers if 10 in customers else cash).remove(10)
                elif 20 in customers + cash and (customers + cash).count(5) >= 5:
                    cash.append(50)
                    for _ in range(5):
                        (customers if 5 in customers else cash).remove(5)
                    (customers if 20 in customers else cash).remove(20)
                elif (customers + cash).count(10) >= 4:
                    cash.append(50)
                    for _ in range(4):
                        (customers if 10 in customers else cash).remove(10)
                    (customers if 5 in customers else cash).remove(5)
                elif (customers + cash).count(10) >= 3 and (customers + cash).count(5) >= 3:
                    cash.append(50)
                    for _ in range(3):
                        (customers if 10 in customers else cash).remove(10)
                    for _ in range(3):
                        (customers if 5 in customers else cash).remove(5)
                elif (customers + cash).count(10) >= 2 and (customers + cash).count(5) >= 4:
                    cash.append(50)
                    for _ in range(2):
                        (customers if 10 in customers else cash).remove(10)
                    for _ in range(4):
                        (customers if 5 in customers else cash).remove(5)
                elif 10 in customers + cash and (customers + cash).count(5) >= 7:
                    cash.append(50)
                    for _ in range(7):
                        (customers if 5 in customers else cash).remove(5)
                    (customers if 10 in customers else cash).remove(10)
                elif (customers + cash).count(5) >= 9:
                    cash.append(50)
                    for _ in range(9):
                        (customers if 5 in customers else cash).remove(5)
                else:
                    return False
            else:
                return False
    return True


def can_sell_icecream2(queue: list[int]) -> bool:
    cash = {5: 0, 10: 0, 20: 0, 50: 0}  # Считаем количество банкнот в кассе

    # Перебираем все банкноты покупателя в очереди, увеличиваем их количество в кассе
    for banknote in queue:
        cash[banknote] += 1

    # Отладочная печать: показывает текущую очередь и состояние кассы после первой итерации
    print(queue)
    print(cash)

    # Обработка каждой банкноты с учётом сдачи
    for banknote in queue:
        if banknote == 10:  # Если банкнота 10
            if cash[5] <= 0:
                return False  # Нельзя выдать сдачу десяткой без пятёрки
            cash[5] -= 1  # Уменьшаем количество пятёрок на 1
        elif banknote == 20:  # Если банкнота 20
            if cash[10] > 0 and cash[5] > 0:  # При наличии десятки и пятёрки
                cash[10] -= 1
                cash[5] -= 1
            elif cash[5] >= 3:  # Если нет десятки, но есть 3 пятёрки
                cash[5] -= 3
            else:
                return False  # Невозможно дать сдачу для 20
        elif banknote == 50:  # Если банкнота 50
            # Пытаемся выдать сдачу комбинациями из банкнот 20, 10 и 5
            if cash[20] >= 2 and cash[5] > 0:  # 2 банкноты по 20 и одна пятёрка
                cash[20] -= 2
                cash[5] -= 1
            elif cash[20] > 0 and cash[10] >= 2 and cash[5] > 0:  # 1 по 20, 2 по 10, одна 5
                cash[20] -= 1
                cash[10] -= 2
                cash[5] -= 1
            elif cash[10] >= 4 and cash[5] >= 0:  # 4 по 10 и одна 5
                cash[10] -= 4
                cash[5] -= 1
            elif cash[10] >= 3 and cash[5] >= 3:  # 3 по 10 и 3 пятёрки
                cash[10] -= 3
                cash[5] -= 3
            elif cash[10] >= 2 and cash[5] >= 5:  # 2 по 10 и 5 пятёрок
                cash[10] -= 2
                cash[5] -= 5
            elif cash[10] >= 1 and cash[5] >= 7:  # 1 по 10 и 7 пятёрок
                cash[10] -= 1
                cash[5] -= 7
            elif cash[5] >= 9:  # 9 пятёрок
                cash[5] -= 9
            else:
                return False  # Невозможно дать сдачу для 50
    return True  # Если прошли очередь и дали сдачу всем, значит всё хорошо



print('False = ', can_sell_icecream2([50, 20, 10, 5, 5, 5]), '\n')  # False
print('False = ', can_sell_icecream2([50, 10, 10, 10, 10, 5]), '\n')  # False
print('True = ', can_sell_icecream2([20, 5, 5, 5, 5]), '\n')  # True
print('False = ', can_sell_icecream2([5, 10, 10]), '\n')  # False
print('True = ', can_sell_icecream2([5, 5, 10, 10]), '\n')  # True
print('True = ', can_sell_icecream2([5, 10, 5, 20]), '\n')  # True
print('True = ', can_sell_icecream2([5, 5, 5, 20]), '\n')  # True
print('False = ', can_sell_icecream2([50, 10, 5, 20, 10, 10, 5, 5, 5]), '\n')  # False
print('True = ', can_sell_icecream2([50, 10, 5, 20, 10, 10, 5, 5, 5, 5]))  # True


# def can_sell_icecream3(queue: list[int]) -> bool:
#     if 10 in queue:
#         if queue.count(5) < queue.count(10):
#             return False
#         else:
#             for _ in range(queue.count(10)):
#                 queue.remove(10)
#                 queue.remove(5)
#     if 20 in queue:
#         if (
#                 queue.count(10) < queue.count(20) and
#                 queue.count(5) * 3 < (queue.count(20))
#         ):
#             if 10 in queue:
#                 for _ in range(queue.count(20)):
#                     queue.remove(10)
#                     queue.remove(5)
#             else:
#                 for _ in range(queue.count(20)):
#                     queue.remove(5)
#                     queue.remove(5)
#                     queue.remove(5)
#         else:
#             return False
#
#     if 50 in queue:
#         if (
#             queue.count(20) * 2 < queue.count(50) and
#             queue.count(10) * 4 < queue.count(50) and
#             queue.count(5) * 9 < queue.count(50) and
#             queue.count(20)
#         ):
#             if 20 >= 2:
#                 for _ in range(queue.count(50)):
#                     queue.remove(20)
#                     queue.remove(20)
#                     queue.remove(5)
#             elif 10 >= 2:
#     return True
#
# print(can_sell_icecream3([10, 5, 20, 5, 5]))