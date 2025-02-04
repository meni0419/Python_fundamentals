def factorial(n):
    """
    1. Написать программу, вычисляющую факториал числа.
    Решить задачу с помощью рекурсии."""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)  # 5 × 4 × 3 × 2 × 1 = 120`


print(f"Factorial: {factorial(5)}")
