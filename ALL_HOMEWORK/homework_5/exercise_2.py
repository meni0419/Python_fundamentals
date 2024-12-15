def leap_year_checker(year_to_check):
    if year_to_check % 4 == 0 and year_to_check % 100 != 0 or year_to_check % 400 == 0:
        return True
    else:
        return False


year = int(input("Enter year: "))
if leap_year_checker(year):
    print("Leap year")
else:
    print("Not leap year")
