# 1
from itertools import product


def prints_str_p5_1():
    str_p5_1 = input("Input a string: ")

    print(f"a. {str_p5_1[2]} \n"
          f"b. {str_p5_1[-2]} \n"
          f"c. {str_p5_1[:5]} \n"
          f"d. {str_p5_1[:-2]} \n"
          f"e. {str_p5_1[::2]} \n"
          f"f. {str_p5_1[1::2]} \n"
          f"g. {str_p5_1[::-1]} \n"
          f"h. {str_p5_1[::-2]} \n"
          f"i. {len(str_p5_1)}")


# 2
def price_in_euro_p5_1():
    product_p5_1 = input("Enter product: ")
    price_p5_1 = float(input("Enter price: "))
    print(f"The price of {product_p5_1} is {price_p5_1:.2f} euro")


# 3
def count_words_p5_1():
    str_p5_1 = input("Enter string: ")
    print(f"The number of words in the string is {str_p5_1.count(' ') + 1}")
    print(f"The number of words in the string is {len(str_p5_1.split(" "))}")


# 4
def count_substrings_p5_1():
    str_p5_1 = input("Enter string: ")
    substr_p5_1 = input("Enter substring: ")
    str_p5_1 = str_p5_1.lower()
    print(f"The number of substrings in the string is {str_p5_1.count(substr_p5_1)}")


# 5
def rearrange_p5_1():
    str_p5_1 = input("Enter string: ")
    print("{1} {0}".format(str_p5_1.split(" ")[0], str_p5_1.split(" ")[1]))
    print(f"{str_p5_1.split(" ")[1]} {str_p5_1.split(" ")[0]}")
    print("%s %s" % (str_p5_1.split(" ")[1], str_p5_1.split(" ")[0]))


# 6
def index_letter_in_str_p5_1():
    str_p5_1 = input("Enter string: ")
    letter_p5_1 = input("Enter letter: ")
    if letter_p5_1 in str_p5_1:
        if str_p5_1.count(letter_p5_1) > 1:
            print(f"The first index of the letter \"{letter_p5_1}\" in the string is [{str_p5_1.index(letter_p5_1)}] "
                  f"and last index is [{str_p5_1.rindex(letter_p5_1)}]")
        else:
            print(f"The index of the letter \"{letter_p5_1}\" in the string is [{str_p5_1.index(letter_p5_1)}]")
    else:
        print(f"The letter \"{letter_p5_1}\" not in the string")


# 7
def replace_numebrs_p5_1():
    str_p5_1 = "1 of the another 1"
    str_p5_1 = str_p5_1.replace("1", "one")
    print(str_p5_1)
