#Используя метод find(), найдите позицию слова Mars в строке:
#Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.

# text = "Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."
# print(text.find("Mars"))

text = """daylight: 260 F Nighttime: -280 F
   nighttime: -280 F
nighttime: -280 F
daylight:      260 F
daylight: 260 F"""
string = text.split("\n")
i = 0
while i < len(string):
    string[i] = " ".join(string[i].split()).capitalize()
    i += 1

text = "\n".join(string)
print(text)

# t= text.split()
# print(*t)

# t = " ".join(t)
# print(t)

bearer = 'curl - X GET http://127.0.0.1:8000/employees/ -H \"Authorization: Bearer some_token\"'

cookie = "curl - X GET http://127.0.0.1:8000/employees/ --cookie \"access_token=some_token\""