def first_n_number_from_fibonacci(n):
    a, b = 0, 1
    s = ""
    while n > 0:
        s += f", {a}" if s else f"{a}"
        a, b = b, a + b
        n -= 1
    return s


N = int(input("Enter number: "))
print(f"First {N} numbers from fibonacci sequence: {first_n_number_from_fibonacci(N)}")