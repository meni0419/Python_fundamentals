# #1 This program predicts the appropriate recommendation based on current weather conditions.
# def weather_prediction(rain, snow, wind, cloudy):
#     # Return a recommendation if there is no precipitation or wind.
#     if rain == "no" and cloudy == "no" and snow == "no" and wind == "no":
#         return "go for a walk."
#     # Return a recommendation to take an umbrella if it is raining or cloudy without snow or wind.
#     elif (rain == "yes" or cloudy == "yes") and snow == "no" and wind == "no":
#         return "take an umbrella."
#     # Return a recommendation to take an umbrella and put on a jacket if it is snowing along with rain or cloudy weather.
#     elif (rain == "yes" or cloudy == "yes") and snow == "yes" and wind == "no":
#         return "take an umbrella, put on a jacket."
#     # Return a recommendation to take an umbrella and put on a coat if there is strong wind along with rain or cloudy weather.
#     elif (rain == "yes" or cloudy == "yes") and snow == "no" and wind == "yes":
#         return "take an umbrella, put on a coat."
#     # Recommend staying at home for any other adverse weather condition.
#     else:
#         return "Are you mind? Stay at home."
#
#
# # Gather user input for various weather conditions.
# rain_is_falling = input("Is it raining? ")
# snow_is_falling = input("Is it snowing? ")
# strong_wind = input("Is there a strong wind? ")
# is_cloudy = input("Is it cloudy? ")
#
# # Display the prediction based on the provided weather inputs.
# print(weather_prediction(rain_is_falling, snow_is_falling, strong_wind, is_cloudy))

# #2 exercise
# def put_on_shoes():
#     rain_now = input("Is it raining now? ")
#     if rain_now == "no" or "No":
#         rain_last = input("Did it rain last night? ")
#         if rain_last == "yes" or "Yes":
#             return "put on your boots anyway"
#         else:
#             return "put on your sneakers"
#     else:
#         return "ok, put on your boots"
#
#
# print(put_on_shoes())

# #3 This program determines which months correspond to a given number of days in a month.
# def which_month(days):
#     if days == 31:
#         return "January, March, May, July, August, October, December"
#     elif days == 28 or days == 29:
#         return "February"
#     elif days == 30:
#         return "April, June, September, November"
#     else:
#         return "Error: Invalid input. Valid values are 28, 29, 30, or 31."
#
# try:
#     days_in_month = int(input("Enter the number of days in a month (28, 29, 30, or 31): "))
#     if days_in_month not in [28, 29, 30, 31]:
#         raise ValueError("Invalid range")
#     print(which_month(days_in_month))
# except ValueError:
#     print("Error: Please enter a valid number (28, 29, 30, or 31).")

def what_gen_year(y):
    if y <= 1965:
        return "Baby-boomers"
    elif 1966 <= y <= 1980:
        return "Generate X"
    elif 1981 <= y <= 1996:
        return "Generate Y (Millennial's)"
    elif y > 1996:
        return "Generate Z"


year = int(input("Enter year: "))
print(what_gen_year(year))