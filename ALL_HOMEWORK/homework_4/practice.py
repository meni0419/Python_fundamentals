# def unique_num(a,b,c):
#     if a==b or a==c or b==c:
#         print("Numbers is not unique")
#     else:
#         print("Numbers is unique")
#
# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# n3 = int(input("Enter third number: "))
#
# unique_num(n1,n2,n3)

def unique_num(a, b, c):
    if a != b and a != c and b != c:
        print("Numbers is unique")
    else:
        print("Numbers is not unique")


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

unique_num(n1, n2, n3)
