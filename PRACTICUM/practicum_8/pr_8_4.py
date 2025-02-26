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


def can_sell_icecream_v2(lst: list[int]) -> bool:
    cash = []
    customers = lst.copy()
    for banknote in lst:
        if banknote in customers:
            if banknote == 5 and 5 in customers:
                cash.append(5)
                customers.remove(5)
            if banknote == 10 and 5 in customers + cash:
                (customers if 5 in customers else cash).remove(5)
                cash.append(10)
            elif banknote == 10 and 5 not in customers + cash:
                return False
            elif banknote == 20 and 5 in customers + cash:
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
            elif banknote == 50 and 5 in customers + cash:
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
    return True


def can_sell_icecream(queue: list[int]) -> bool:
    cash = []

    def take_change(amount: int) -> bool:
        """Обрабатывает сдачу, используя cash и customers."""
        nonlocal cash
        for banknote in [20, 10, 5]:  # Проверяем сдачу от крупных к мелким
            while amount >= banknote and banknote in cash + customers:
                target = customers if banknote in customers else cash
                target.remove(banknote)
                amount -= banknote
        return amount == 0  # Вернём True, если удалось полностью покрыть сдачу

    customers = queue.copy()
    for banknote in queue:
        if banknote == 5:
            cash.append(5)
            customers.remove(5)
        elif banknote in [10, 20, 50]:
            # Рассчитаем сдачу: для 10 нужно вернуть 5, для 20 — 15, для 50 — 45
            if not take_change(banknote - 5):
                return False
            cash.append(banknote)
            customers.remove(banknote)
    return True


print(can_sell_icecream([50, 20, 10, 5, 5, 5]))  # True
print(can_sell_icecream([50, 10, 10, 10, 10, 5]))  # True
print(can_sell_icecream([20, 5, 5, 5, 5]))  # True
print(can_sell_icecream([5, 10, 10]))  # False
print(can_sell_icecream([5, 5, 10, 10]))  # True
print(can_sell_icecream([5, 10, 5, 20]))  # True
print(can_sell_icecream([5, 5, 5, 20]))  # True
print(can_sell_icecream([50, 10, 5, 20, 10, 10, 5, 5, 5]))  # False
print(can_sell_icecream([50, 10, 5, 20, 10, 10, 5, 5, 5, 5]))  # True
