from decimal import Decimal, getcontext
from math import sqrt, pi


# 1
def print_name():
    str_name = "Max"
    print(f"Hello {str_name}")


# 2
def wrap_text_with_tag():
    tag = "i"
    text = "Hello"
    print(f"<{tag}>{text}</{tag}>")


# 3
def multiply_char():
    stroka = "Hello"
    print(stroka[-2::] * 3)


# 4
def print_str_without_char():
    str1 = "Hello"
    print(str1[1:-1])


# 5
def print_str_with_char():
    str1 = "Hello"
    str2 = "hi"
    if len(str1) > len(str2):
        print(str2 + str1 + str2)
    else:
        print(str1 + str2 + str1)


# 6
def is_cat_count_eq_dog_in_str():
    user_str = input("Enter string: ")
    str1 = "cat"
    str2 = "dog"
    if user_str.count(str1) == user_str.count(str2):
        print("True")
    else:
        print("False")


# 7
def count_word_in_str():
    user_substr = input("Enter substring: ")
    user_str = input("Enter string: ")
    print(user_str.count(user_substr))


# 8
def multiply_echars_in_str():
    user_str = input("Enter string: ")
    for i in user_str:
        user_str = user_str.replace(i, i * 2)
    print(user_str)


# 9
def len_of_hypotenuse():
    leg1 = int(input("Enter leg1: "))
    leg2 = int(input("Enter leg2: "))
    print(f"{sqrt(leg1 ** 2 + leg2 ** 2):.2f}")


# 10
def sphere_calc():
    radius_sph = float(input("Enter radius sphere: "))
    length_sph = 2 * pi * radius_sph
    s_sph = pi * radius_sph ** 2
    volume_sph = 4 / 3 * pi * radius_sph ** 3
    print(f"length {length_sph:.2f}\n"
          f"S {s_sph:.2f}\n"
          f"volume {volume_sph:.2f}")


# 11
def sum_of_decimal_prec():
    getcontext().prec = 2
    n1 = float(input("Enter a: "))
    n2 = float(input("Enter b: "))
    n3 = float(input("Enter b: "))
    n4 = float(input("Enter b: "))
    n5 = float(input("Enter b: "))
    sum_a_b = Decimal(n1) + Decimal(n2) + Decimal(n3) + Decimal(n4) + Decimal(n5)
    print(sum_a_b)


def sum_of_decimal():
    n1 = float(input("Enter a: "))
    n2 = float(input("Enter b: "))
    n3 = float(input("Enter b: "))
    n4 = float(input("Enter b: "))
    n5 = float(input("Enter b: "))
    sum_a_b = Decimal(n1) + Decimal(n2) + Decimal(n3) + Decimal(n4) + Decimal(n5)
    print(f"{sum_a_b:.1f}")
