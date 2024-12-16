# function for transform decimal number to binary
def decimal_to_binary(d):
    b = ""
    # while entered number greater than 0 we calculate its remainder and divide it into integers
    while d > 0:
        b = str(d % 2) + b
        d = d // 2
    return b

# output results decimal to binary
decimal = int(input("decimal number:"))
binary = decimal_to_binary(decimal)
print(f"binary: {binary}")