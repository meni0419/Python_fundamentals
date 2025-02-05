line = """    \thello,,,, world.    how are you???    """
PUNCTUATION_MARKS_AND_SPACE = " ,.:;!?"
new_line = ""
j = 0
while j < len(line) - 1:  # делаем цикл по длине предложения, но -1 т.к. потом делаем замену +1 индекс
    j += 1
    if line[j] == line[j - 1] and (line[j] in PUNCTUATION_MARKS_AND_SPACE):
        continue
    new_line += line[j]

print(new_line)
