def count_even_numbers():
    a = int(input("Enter a number N for counting: \n"))
    b = int(input("Enter a number M for compare: \n"))
    c = 0
    count = 0
    while a > 0:
        c = a % 10
        if c % 2 == 0 and c <= b:
            count += 1
        a = a // 10
    return count


print(f"{count_even_numbers()} even numbers <= M in N")
