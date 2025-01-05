"""
1. Напишите программу, которая запрашивает у пользователя его имя, возраст и место проживания, а затем выводит их в
следующем формате:

"Привет, меня зовут {0}. Мне {1} лет. Я живу в {2}."

Вместо {0}, {1} и {2} подставьте соответствующие значения. Используйте метод format() для форматирования строки.
Потом попробуйте использовать f-строку. Выведите результат на экран с помощью команды print.
"""

def who_how_where():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    place = input("Enter your place: ")
    print("Hello, my name is {}. I am {} years old. I live in {}.".format(name, age, place))
    print(f"Hello, my name is {name}. I am {age} years old. I live in {place}.")

#who_how_where()

"""
2. Напишите программу, которая запрашивает у пользователя два числа и выводит их сумму и произведение в следующем формате:

"Сумма: {sum:.2f}, Произведение: {product:.2f}"

Вместо {sum:.2f} и {product:.2f} подставьте соответствующие значения, округленные до двух десятичных знаков. 
Используйте f-строки с использованием форматных спецификаторов для форматирования чисел. Выведите результат на экран 
с помощью команды print.
"""

def sum_product():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Sum: {:.2f}, Product: {:.2f}".format(a + b, a * b))
    print(f"Sum: {a + b:.2f}, Product: {a * b:.2f}")

sum_product()