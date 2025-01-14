"""
not (A and B) == not A or not B
not (A or B) == not A and not B

not ((A or B) and (C or D)) == ((not A and not B) or (not C and not D))

E = (A or B)
F = (C or D)

not (E and F) == not E or not F == (not (A or B)) or (not (C or D)) == (not A and not B) or (not C and not D)
"""


