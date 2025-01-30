from decimal import Decimal, getcontext

# Set the precision for Decimal operations
getcontext().prec = 28

# Function to calculate the sum of the Leibniz series
def sum_of_leibniz(n=1000):
    i = Decimal('3')  # Denominator starts at 3
    s_sum = Decimal('1')  # Initial sum starts with 1
    plus = False  # Toggle for addition and subtraction

    # Loop through n iterations of the series
    while n > 0:
        if plus:
            s_sum += Decimal('1') / i  # Add term to the sum
            plus = False
        else:
            s_sum -= Decimal('1') / i  # Subtract term from the sum
            plus = True
        i += Decimal('2')  # Increment the denominator by 2
        n -= 1  # Decrement the count

    return s_sum  # Return the calculated sum

print(sum_of_leibniz())
# Prompt the user for input and validate it
# try:
#     num = int(input("Enter a positive integer for the number of terms: "))
#     if num <= 0:
#         raise ValueError("The number must be a positive integer.")
#     # Print the result of the calculated Leibniz sum
#     print(f"Sum of first {num} terms of the Leibniz series: {sum_of_leibniz(num)}")
# except ValueError as e:
#     # Handle cases where the input is invalid
#     print(f"Invalid input: {e}")
