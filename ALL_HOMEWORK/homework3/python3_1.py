# function for simple calc
def simple_calc(a, b):
    summ_a_b = a + b
    diff_a_b = a - b
    mult_a_b = a * b
    divide_a_b = a / b
    rem_a_b = a % b
    pow_a_b = a ** b

    # could have been used just print but return more functionality
    return summ_a_b, diff_a_b, mult_a_b, divide_a_b, rem_a_b, pow_a_b


x1 = int(input("x1: "))
x2 = int(input("x2: "))

# call the function
summ, diff, mult, divide, rem, pow1_in_2 = simple_calc(x1, x2)

# output
print(f"Sum: {summ}"
      f"\nDiff: {diff}"
      f"\nMultiply: {mult}"
      f"\nDivide: {divide}"
      f"\nReminder: {rem}"
      f"\nPow a in b: {pow1_in_2}")
