def check_simple_num(num):
    i = num
    s = 0
    while i > 0:
        if num % i == 0:
            s += 1
        i -= 1
    if s == 2:
        print(f"Number {num} is simple")
    else:
        print(f"Number {num} is not simple")


number = int(input("Enter number: "))
check_simple_num(number)
