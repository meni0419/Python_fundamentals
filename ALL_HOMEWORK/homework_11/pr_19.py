text = 'Bearer command: curl - X GET http://127.0.0.1:8000/employees/ -H \"Authorization: Bearer some_token\"'
word = 'Bearer'


def find_indices(text, word):
    index_found = []
    i = 0
    while i < len(text):
        i = text.lower().find(word.lower(), i)
        if i == -1:
            break
        index_found.append(i)
        i += len(word)
    return index_found


print(*find_indices(text, word))


def find_indices2(text, word):
    index_found = ""
    i = 0
    while i < len(text):
        i = text.lower().find(word.lower(), i)
        if i == -1:
            break
        index_found += str(i) + " "
        i += len(word)
    return index_found


print(find_indices2(text, word))


