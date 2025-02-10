"""
Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n пингвинов.
Изображение одного пингвина имеет размер 5×9 символов, между двумя соседними пингвинами
также имеется пустой (из пробелов) столбец. Разрешается вывести пустой столбец после
последнего пингвина. Для упрощения рисования скопируйте пингвина из примера в среду
разработки.
"""


def print_pin(n):
    p1 = "   _~_    "
    p2 = "  (o o)   "
    p3 = " /  V  \\  "
    p4 = "/(  _  )\\ "
    p5 = "  ^^ ^^   "
    if 1 <= n <= 9:
        width_field = 100
        print(f"{p1 * n}".center(width_field))
        print(f"{p2 * n}".center(width_field))
        print(f"{p3 * n}".center(width_field))
        print(f"{p4 * n}".center(width_field))
        print(f"{p5 * n}".center(width_field))
    else:
        print(f"Please, enter number from 1 to 9")

print_pin(5)
#print_pin(int(input("Enter number: ")))
