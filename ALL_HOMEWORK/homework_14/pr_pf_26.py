import timeit

my_list = [1, 2, 3]
# print(id(my_list))
my_list[0] = 10
# print(my_list) # [10, 2, 3]
# print(id(my_list))

# print(f"1st solution: {timeit.timeit("print(my_list[::-1])", globals=globals(), number=1)}")
# print(f"2nd solution: {timeit.timeit("print(list(reversed(my_list)))", globals=globals(), number=1)}")  # more fast
# print(f"3th solution: {timeit.timeit("my_list.reverse(); print(my_list)", globals=globals(), number=1)}")

# numbers = input("Введите числа через пробел: ").split()
# print(numbers)
# numbers = [num.zfill(2) for num in numbers]
# print(numbers)
# numbers = ":".join(numbers)
# print(numbers)

print(
    """1. Выведите на экран треугольник Паскаля для некоторого N тем же способом, что на
    прошлом уроке записывали его в файл.
        a. Решите эту же задачу, используя списки для хранения строк треугольника Паскаля.
        b. С помощью %%timeit сравните время выполнения этих алгоритмов.\n""")


def generate_pascals_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    for row in triangle:
        print(" ".join(map(str, row)))


generate_pascals_triangle(10)
print(
"""\n2. Напишите программу, которая принимает список чисел от пользователя и выводит на 
экран только уникальные числа из списка в порядке их появления. 
Используйте динамический массив для хранения уникальных чисел и методы для 
работы с ним. Выведите результат на экран с помощью команды print.
Пример вывода:
Введите числа, разделенные пробелами: 1 2 3 4 2 3 1 5
Уникальные числа: [1, 2, 3, 4, 5]\n""")


def unique_numbers(numbers):
    numbers_exp = numbers.split()
    numbers_exp = [int(num) for num in numbers_exp]
    for num in numbers_exp:
        if numbers_exp.count(num) > 1:
            numbers_exp.remove(num)
    numbers_exp = list(sorted(numbers_exp))
    return numbers_exp


print(f"result: {unique_numbers("1 2 3 4 2 3 1 5")}")
