def round_float(number):
    if number < 0:
        i_number = int(number)
        r_num = i_number - 1 if (number - i_number) <= -0.5 else i_number
        return r_num
    else:
        i_number = int(number)
        r_num = i_number + 1 if (number - i_number) >= 0.5 else i_number
        return r_num


N = float(input("Enter number: "))
print(round_float(N))