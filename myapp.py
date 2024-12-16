# week = input("Type number of week:")  # give the input field
#
# # list of subject for week 1,2,3
# subjects = {
#     "1": ["Introduction"],
#     "2": ["Python Fundamentals", "Linux", "German", "Databases"],
#     "3": ["Python Fundamentals", "Linux", "Databases", "German"]
# }
#
# # printing the subjects with beauty style
# print("List of subject:")
# for subject in subjects.get(week, "Invalid week number"):
#     print(subject)

# ex1 print 1 + 1 = 2
a = 1
b = 1

print(f"{a} + {b} = {a + b} \n")

# ex2 print list of Subjects for next week
print(f"Subjects for next week: \n"
      f"Python \n"
      f"Fundamentals \n"
      f"Linux \n"
      f"German \n"
      f"Databases")
