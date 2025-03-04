def raising_to_power(lst: list, n: int) -> list:
    return list(map(lambda i: i**n, lst))

def raising_to_power2(x: list, n: int) -> list:
    return [i**n for i in x]


x_ = [1, 2, 3]
n_ = 2
# print(raising_to_power(x_, n_))


def sum_of_even2(*args) -> int:
    sum_ = 0
    for i in args:
        if i % 2 == 0:
            sum_ += i
    return sum_


def sum_of_even(*args) -> int:
    return sum(x for x in args if x % 2 == 0)

# print(sum_of_even(1, 2, 3, 4, 5))

nums = [1, 2, 3, 4, 5]
print([str(x) for x in nums])
print(list(map(float, nums)))