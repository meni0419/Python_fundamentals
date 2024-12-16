week = input("Type number of week:")  # give the input field

# list of subject for week 1,2,3
subjects = {
    "1": ["Introduction"],
    "2": ["Python Fundamentals", "Linux", "German", "Databases"],
    "3": ["Python Fundamentals", "Linux", "Databases", "German"]
}

# printing the subjects with beauty style
print("List of subject:")
for subject in subjects.get(week, "Invalid week number"):
    print(subject)
