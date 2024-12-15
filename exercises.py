# ex 1
def bigger_from_two_number():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if a > b:
        return a
    else:
        return b


# ex 2
def bigger_from_three_number():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    if a > b > c:
        return a
    elif b > c > a:
        return b
    else:
        return c


# print(f"Bigger num: {bigger_from_three_number()}")

# ex 3
def set_bool(var):
    if var.lower() in ['true', '1', 'yes']:
        var = True
    elif var.lower() in ['false', '0', 'no']:
        var = False
    else:
        var = input("Invalid input. Please enter either True or False (e.g., 'True', 'False'): ")
    return var

def is_weekday():
    wday = set_bool(input("Is it weekday? (True/False): "))
    if wday:
        return "weekend"
    else:
        return "workday"


# print(is_weekday())

# ex 4
def can_i_sleep():
    is_weekday = set_bool(input("Is it weekday? (True/False): "))
    is_vacation = set_bool(input("Is it vacation? (True/False): "))

    if is_weekday or is_vacation:
        return "Yes, you can sleep."
    else:
        return "No, you can't sleep."


# print(can_i_sleep())


# ex 5
def diff_num21():
    x = int(input("Enter number: "))
    if x < 21:
        return 21 - x
    else:
        return (x - 21) * 2


# print(diff_num21())

# ex 6
def diff_num100():
    x = int(input("Enter number: "))
    if 10 < x < 100:
        return 100 - x
    else:
        return x


# print(diff_num100())

# ex 7
def have_a_problem():
    monkey1 = set_bool(input("First monkey smile? (True/False): "))
    monkey2 = set_bool(input("Second monkey smile? (True/False): "))

    if (monkey1 and monkey2) or (not monkey1 and not monkey2):
        print("We have a problem.")
    else:
        print("No problem.")


# have_a_problem()

# ex 8
def sum_of_two_num():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    if a == b:
        return (a + b) * 2
    else:
        return a + b


# print(sum_of_two_num())

# ex 9
def num_or_sum_eq10():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    if (a + b) == 10 or a == 10 or b == 10:
        return True
    else:
        return False


# print(num_or_sum_eq10())

# ex 10
def problem_with_parrot():
    is_talking = set_bool(input("Is the parrot talking? (True/False): "))
    hour = int(input("Enter hour: "))
    if hour > 23 or hour < 0:
        hour = int(input("Please, enter hour between 0 and 23:"))
    if is_talking and (hour < 7 or hour > 20):
        return True
    else:
        return False


print(problem_with_parrot())