def count_substrings_p5_4(str_p5_4, substr_p5_1):
    """
    Напишите программу, которая считает вхождение заданной подстроки в заданную строку.
    Например, для подстроки “ab” и строки “Abrakadabra” программа напечатает 2.
    """
    print(f"v1. The number of substrings in the string is {str_p5_4.lower().count(substr_p5_1)}")


str_p5_4 = "Abrakadabra"
substr_p5_1 = "ab"

count_substrings_p5_4(str_p5_4, substr_p5_1)


def search_index(str_p5_4, substr_p5_1):
    return str_p5_4.find(substr_p5_1)


print(f"v3. The index of the 1st entry substring is {search_index(str_p5_4, substr_p5_1)}")
