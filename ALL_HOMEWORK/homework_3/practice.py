def apple_per_schoolchildren(n, k):
    apple = k // n
    basket = k % n
    return apple, basket

s = int(input("schoolchildren: "))
a = int(input("apples: "))
apple_per_sch, in_basket = apple_per_schoolchildren(s, a)
print(f"Apple per schoolchildren {apple_per_sch} and {in_basket} in the basket")

# def operations(n1, n2, n3, n4, fun):
#     if fun == "sum":
#         res = sum([n1, n2, n3, n4])
#         return res
#     elif fun == "multiply":
#         res = n1 * n2 * n3 * n4
#         return res
#     elif fun == "sec":
#         res = n1 * 24 * 60 * 60 + n2 * 60 * 60 + n3 * 60 + n4
#         return res
#
#
# x1 = int(input("x1: "))
# x2 = int(input("x2: "))
# x3 = int(input("x3: "))
# x4 = int(input("x4: "))
# func = input("Type name function: ")
#
# func_result = operations(x1, x2, x3, x4, func)
#
# print(f"Result {x1}, {x2}, {x3}, {x4} in {func} = {func_result}")