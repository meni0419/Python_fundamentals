import math

# function for calc length of circle and area of circle
def pi_r_circle(r):
    length = 2 * math.pi * r
    area = math.pi * (r ** 2)
    return length, area

radius = float(input("Enter radius: "))
length_circle, area_circle = pi_r_circle(radius)

# output calc circle
print(f"length circle: {length_circle}\n"
      f"area_circle: {area_circle}")