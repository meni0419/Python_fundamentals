def binary_to_decimal(b):
    w = 2   # TODO: move to parameters
    dc = 0

    #
    for i in range(len(b)):
        dc += int(b[i]) * (w ** (len(b) - i - 1))
    return dc

binary = input("binary: ")
decimal = binary_to_decimal(binary)
print(f"decimal: {decimal}")

def decimal_to_binary(d):
    binary = ""
    while d > 0:
        binary = str(d % 2) + binary
        d = d // 2
    return binary

decimal = int(input("\ndecimal number:"))
binary = decimal_to_binary(decimal)
print(f"binary: {binary}")