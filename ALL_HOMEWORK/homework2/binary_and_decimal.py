# function for transform binary number to decimal
def binary_to_decimal(b):
    w = 2   # TODO: move to parameters
    dc = 0

    # each num of binary value multiplied on weight raised to the power 2 and sum
    for i in range(len(b)):
        dc += int(b[i]) * (w ** (len(b) - i - 1))
    return dc

# output results binary to decimal
binary = input("binary: ")
decimal = binary_to_decimal(binary)
print(f"decimal: {decimal}")

# function for transform decimal number to binary
def decimal_to_binary(d):
    b = ""

    # while entered number greater than 0 we calculate its remainder and divide it into integers
    while d > 0:
        b = str(d % 2) + b
        d = d // 2
    return b

# output results decimal to binary
decimal = int(input("\ndecimal number:"))
binary = decimal_to_binary(decimal)
print(f"binary: {binary}")