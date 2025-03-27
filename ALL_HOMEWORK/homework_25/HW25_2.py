"""
2. Напишите программу, которая будет считывать данные о продуктах из файла и использовать аннотации типов для аргументов и возвращаемых значений функций. Создайте текстовый файл "products.txt", в котором каждая строка будет содержать информацию о продукте в формате "название, цена, количество". Например:

Apple, 1.50, 10
Banana, 0.75, 15

В программе определите функцию calculate_total_price, которая будет принимать список продуктов и возвращать общую стоимость. Продумайте, какая аннотация должна быть у аргумента! Считайте данные из файла, разделите строки на составляющие и создайте список продуктов. Затем вызовите функцию calculate_total_price с этим списком и выведите результат.

Начиная с этого дз мы потихоньку отказываемся от формата ожидаемого ввода-вывода. Потому что в реальных задачах обычно этого нет. Нужно самому придумывать даже самые простые тестовые данные, содержимое тестовых файлов и т.п. В случае с классами (будут чуть позже) особенно."""


def calculate_total_price(products: list[list[str | float | int]]) -> float:
    total_prod_price = 0
    for product, price, quantity in products:
        total_prod_price += price * quantity
    return total_prod_price


def read_products(filename: str) -> list[list[str | float | int]]:
    products = []
    with open(filename, "r") as file:
        for line in file:
            name, price, quantity = line.split(",")
            products.append([name, float(price), int(quantity)])
    return products


all_products = read_products("products.txt")
total_price = calculate_total_price(all_products)
print(f"Total price: {total_price:.2f}")
