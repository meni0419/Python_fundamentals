from math import prod
"""
1. Напишите программу, которая принимает два числа и возвращает их сумму и произведение в виде кортежа (sum, product).
Используйте функцию для вычисления суммы и произведения. Выведите результат на экран с помощью команды print.
"""

def sum_product(a, b):
    sum_13 = sum([a, b])
    product_13 = prod([a, b])
    return sum_13, product_13

a_13 = int(input("Enter first number: "))
b_13 = int(input("Enter second number: "))

print(f"Sum and product: {sum_product(a_13, b_13)}")


"""
2. Напишите программу, которая принимает список чисел и возвращает сумму, минимальное и максимальное значение из списка. 
Используйте функцию для обработки списка чисел и возврата трех значений. Выведите результат на экран с помощью команды print.
"""

def sum_min_max(list_13):
    sum_13 = sum(list_13)
    min_13 = min(list_13)
    max_13 = max(list_13)
    return sum_13, min_13, max_13

u_list_13 = input("Enter list: ")
u_sum_13, u_min_13, u_max_13 = sum_min_max(eval(u_list_13))
print(f"Sum: {u_sum_13} \n"
      f"Min: {u_min_13} \n"
      f"Max: {u_max_13}")