from decimal import Decimal

# Using the Decimal module to avoid floating-point arithmetic imprecision
x = Decimal("0.1")
y = Decimal("0.2")
z = Decimal("0.3")

print(f"1st solution = {x + y + z}")

# Exploring multiple ways to calculate and present the sum of floating-point numbers
x = 0.1
y = 0.2
z = 0.3

print(f"2nd solution = {round(x + y + z, 2)}")

x = 0.1
y = 0.2
z = 0.3

print(f"3rd solution = {x + y + z:.2f}")

x = 0.1
y = 0.2
z = 0.3

print(f"4th solution = {x + y + z:.2}")


# Function to convert time (hours and minutes) into total seconds
def hour_and_min_to_sec(h, m):
    return h * 3600 + m * 60


# Taking user input for hours and minutes and converting to seconds
hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))

print(f"Total time in seconds: {hour_and_min_to_sec(hours, minutes)}")
