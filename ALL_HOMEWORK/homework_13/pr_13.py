with open('input.txt', 'r') as input_file:
    listrows = input_file.readlines()

with open('output.txt', 'a') as output_file:  # Open output.txt once
    for row in listrows:
        words_list = list(reversed(row.strip().split(' ')))
        for word in words_list:
            output_file.write(word + '\n')
