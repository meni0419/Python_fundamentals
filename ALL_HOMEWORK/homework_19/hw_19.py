l1 = [2, 4, 3]
l2 = [5, 6, 4]
# l1 = [0]
# l2 = [0]
# l1 = [9,9,9,9,9,9,9]
# l2 = [9,9,9,9]
def reverse(l):
    r = []
    while l:
        r.append(l.val)
        l = l.next
    return int(''.join(l[::-1]))

print(reverse(l1))

# r2 = int(''.join(map(str, l2[::-1])))
# sum_r = r2
#
# i = 0
# sum_list = []
# j = len(str(sum_r))
# while i < len(str(sum_r)) and j >=0:
#     sum_list.append(int(str(sum_r)[j-1]))
#     i += 1
#     j -= 1
#print(sum_list)

#print(list(map(int, str(sum_r)[::-1])))

# Example 2:
# Output: [0]

# Example 3:
# Output: [8,9,9,9,0,0,0,1]
