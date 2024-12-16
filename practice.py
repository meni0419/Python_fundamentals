def float_to_binary(num):
    # Handle sign (0 for positive, 1 for negative)
    sign = 0
    if num < 0:
        sign = 1
        num = -num  # Work with the magnitude of the number

    # Handle special cases: zero
    if num == 0:
        return "0" * 32  # 32 bits of all zeroes

    # Handle the exponent and mantissa:
    exponent = 0
    # Normalize the number to be in the range [1, 2) and count the shifts
    while num >= 2:
        num /= 2
        exponent += 1
    while num < 1:
        num *= 2
        exponent -= 1

    # Bias the exponent by 127 (per IEEE 754 standard)
    exponent += 127

    # Extract the fraction (mantissa) by removing the leading 1 (implicit)
    mantissa = num - 1

    # Convert exponent and mantissa to binary
    exponent_bits = ""
    for _ in range(8):  # 8 bits for the exponent
        exponent_bits = str(exponent % 2) + exponent_bits
        exponent //= 2

    mantissa_bits = ""
    for _ in range(23):  # Only 23 bits for the mantissa
        mantissa *= 2
        if mantissa >= 1:
            mantissa_bits += "1"
            mantissa -= 1
        else:
            mantissa_bits += "0"

    # Combine sign, exponent, and mantissa
    binary_representation = str(sign) + exponent_bits + mantissa_bits

    return binary_representation


# Ask the user for a real number
user_input = float(input("Enter a decimal number: "))
print(f"Representation of a number {user_input} in IEEE 754 format: {float_to_binary(user_input)}")
