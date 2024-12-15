A = True
B = False
C = True
D = False

equaled1 = not ((A or B) and (C or D)) == ((not A and not B) or (not C and not D))

print(equaled1)
