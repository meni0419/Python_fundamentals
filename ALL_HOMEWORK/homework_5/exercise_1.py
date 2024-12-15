# def sort_numbers(a, b, c):
#     return sorted([a, b, c])
#
#
# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# n3 = int(input("Enter third number: "))
#
# print(*sort_numbers(n1, n2, n3), sep=", ")

# This function prints the three input numbers in ascending order.
def sort_numbers(a, b, c):
    if a < b < c:
        print(f"Numbers by sort ask: {a}, {b}, {c}")
    elif a < c < b:
        print(f"Numbers by sort ask: {a}, {c}, {b}")
    elif b < a < c:
        print(f"Numbers by sort ask: {b}, {a}, {c}")
    elif b < c < a:
        print(f"Numbers by sort ask: {b}, {c}, {a}")
    elif c < a < b:
        print(f"Numbers by sort ask: {c}, {a}, {b}")
    elif c < b < a:
        print(f"Numbers by sort ask: {c}, {b}, {a}")


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

sort_numbers(n1, n2, n3)
