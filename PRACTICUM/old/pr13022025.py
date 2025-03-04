# хотите задачку на рекурсию? Одна из тех, что мне вчера чат GPT дал.
# Дан список, элементами которого могут быть числа и списки с бесконечной вложенностью.
# Вернуть сумму всех чисел   этого списка. Через рекурсию.
# Например [1, 2, 3, [1, 1, [1, 2],1], 1, 1]
# должно вернуть 14

def sum_list(lst, summ=0):
    if not lst:
        return summ
    return sum_list(lst[1:],
                    summ + (lst[0] if isinstance(lst[0], int) else sum(
                        [i if isinstance(i, int) else sum(i) for i in lst[0]])))


print(sum_list([1, 2, 3, [1, 1, [1, 2], 1], 1, 1]))


# lst = [[1, 1, [1, 2],1], 1, 1]
# a = [i if type(i) == int else sum(i) for i in lst[0]]
# print(sum(a))


def sum_list_GPT(lst, summ=0):
    if not lst:
        return summ
    return sum_list_GPT(lst[1:],
                        summ + (lst[0] if isinstance(lst[0], int) else sum_list_GPT(lst[0], 0)))


print(sum_list_GPT([1, 2, 3, [1, 1, [1, 2], 1], 1, 1]))
