"""
Дано предложение и количество раз которое его надо повторить. Напишите программу,
которая повторяет данное предложение нужное количество раз.
Формат входных данных:
В первой строке записано текстовое предложение, во второй — количество повторений.
Формат выходных данных:
Программа должна вывести указанное текстовое предложение нужное количество раз.
Каждое повторение должно начинаться с новой строки.
"""


def multiply_rows(text, n):
    for i in range(n):
        print(text)


text = "Дано предложение"
n = 3

multiply_rows(text, n)
#multiply_rows(text=input("Enter text: "), n=int(input("Enter number: ")))
