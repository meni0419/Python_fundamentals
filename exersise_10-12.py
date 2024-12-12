from math import sqrt

"""
Calculate the length of the hypotenuse of a right triangle 
given the lengths of the two legs.
"""


def length_of_hypotenuse(a, b):
    return sqrt(a ** 2 + b ** 2)


leg1 = float(input("Enter 1st leg: "))
leg2 = float(input("Enter 2nd leg: "))

print(f"Length of hypotenuse is: {length_of_hypotenuse(leg1, leg2):.2f}")