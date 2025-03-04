lst = [1, 2, 3, 4, 5, 3]
# count = []
# for i in lst:
#     if i == 3:
#         count.append(lst.index(i))

count = len([i for i in lst if i == 3])
print(count)




# a = "123"
#
# print(list(a))
#
# a = {1, 2, 3}
# print(list(a))
#
# x = [x for x in range(1, 4)]
# print(x)


def is_valid_parentheses(s: str) -> bool:
    stack = []
    if s.count('(') != s.count(')'):
        return False

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif len(stack) > 0:
            stack.pop()
        else:
            return False
    return True


# print(is_valid_parentheses("()") == True)      # True
# print(is_valid_parentheses("(())") == True)    # True
# print(is_valid_parentheses("(()") == False)    # True
# print(is_valid_parentheses(")(") == False)     # True
# print(is_valid_parentheses("())(") == False)   # True