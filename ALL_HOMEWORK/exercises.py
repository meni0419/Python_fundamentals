# 1
import math


def count_even_numbers():
    a = int(input("Enter a number N for counting: \n"))
    b = int(input("Enter a number M for compare: \n"))
    c = 0
    count = 0
    while a > 0:
        c = a % 10
        if c % 2 == 0 and c <= b:
            count += 1
        a = a // 10
    return count


# print(f"{count_even_numbers()} even numbers <= M in N")

# 2
def num_of_fibonacci():
    n = int(input("Enter number: "))
    a, b = 0, 1
    if n == 0 or n == 1:
        return a
    else:
        while (n - 1) > 0:
            a, b = b, a + b
            n -= 1
        return a


# print(f"Number of fibonacci sequence: {num_of_fibonacci()}")

# 3
def max_power_of_two():
    n = int(input("Enter number: "))
    if n == 0:
        return 0
    else:
        pnum = 0
        maxpow = 0
        while pow(2, pnum) < n:
            maxpow = pow(2, pnum)
            pnum += 1
        return maxpow, pnum - 1


# print(f"Max power of two: {max_power_of_two()}")

# 4
def natural_divisor():
    n = int(input("Enter number: "))
    if n < 1:
        n = int(input("Please enter number > 1: "))
    i = 2
    while n % i != 0:
        i += 1
    return i


# print(f"least natural divisor: {natural_divisor()}")


# 5
def sum_of_digits():
    number = abs(int(input("Enter number: ")))
    if number == 0:
        return 0
    i = 0
    s_d = 0
    while str(number)[i] != '0':
        if i == len(str(number)) - 1:
            break
        s_d += int(str(number)[i])
        i += 1
    return s_d


# print(f"Sum of digits before 0: {sum_of_digits()}")

# 6
def avg_of_digits():
    number1 = abs(int(input("Enter number: ")))
    if number1 == 0:
        return 0
    i = 0
    a_d = 0
    while str(number1)[i] != '0':
        if i == len(str(number1)) - 1:
            break
        a_d += int(str(number1)[i])
        i += 1
    return a_d / i


# print(f"Average of digits before 0: {avg_of_digits()}")

# 7
def max_of_digits():
    number2 = abs(int(input("Enter number: ")))
    if number2 == 0:
        return 0
    i = 0
    m_d = 0
    while str(number2)[i] != '0':
        if i == len(str(number2)) - 1:
            break
        if m_d > int(str(number2)[i]):
            i += 1
        else:
            m_d = int(str(number2)[i])
            i += 1
    return m_d


# print(f"Max of digits before 0: {max_of_digits()}")

# 8
def index_of_max_digits():
    num = abs(int(input("Enter number: ")))
    if num == 0:
        return 0
    i = 0
    index = 0
    max_n = 0
    if int(str(num)[i]) == 0:
        return 0
    else:
        while int(str(num)[i]) != 0:
            if i == len(str(num)) - 1:
                break
            if max_n > int(str(num)[i]):
                i += 1
            else:
                max_n = int(str(num)[i])
                index = i
                i += 1
        return index


# print(f"Index of max digits before 0: {index_of_max_digits()}")

# 9
def r_of_v():
    v = int(input("Enter V sphere: "))
    r = ((3 * v) / (4 * math.pi)) ** (1 / 3)
    return r


# print(f"Radius of V sphere: {r_of_v()}")

# 10
def round_float():
    number = float(input("Enter number: "))
    a = round(number, 2)
    b = round(number, 3)
    return a, b


# print(f"Round float: {round_float()}")

# 11
def eqv_1_2_3():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    tolerance = 0.0001 * max(a, b)
    t_f = abs(((a + b) - c)) <= tolerance
    return t_f


print(f"Are a + b = c? {eqv_1_2_3()}")
