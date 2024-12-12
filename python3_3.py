# function instead of sqrt()
def sqrt(res):
    sqrt_res = res ** 0.5
    return sqrt_res


# function for calc distance between coords
def calc_distance(x1, y1, x2, y2):
    distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


try:
    # simplify of type coords
    cx1, cy1 = map(float, input("Enter coords1: ").split(","))
    cx2, cy2 = map(float, input("Enter coords2: ").split(","))
    # calc distance between coords
    distance_coords = calc_distance(cx1, cy1, cx2, cy2)
    # output calc distance
    print(f"Distance between coords: {distance_coords}")
except ValueError:  # error handling
    print("Please, enter 2 coords x,y. Example: 2,3")
