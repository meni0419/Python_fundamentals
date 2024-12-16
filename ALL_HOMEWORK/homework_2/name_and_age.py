import datetime

name = input("Enter your name: ")
year_of_b = input("Enter your year of birthday: ")

age = datetime.datetime.now().year - int(year_of_b)

print(f"Hello, {name}! You are {age} years old")