def index_letter_in_str_p5_6(str_p5_6, letter_p5_1):
    """
    Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс.
    Если она встречается два и более раз, выведите индекс ее первого и последнего появления.
    Если буква f в данной строке не встречается, ничего не выводите.
    При решении этой задачи не стоит использовать циклы.

    """
    if letter_p5_1 in str_p5_6:
        if str_p5_6.count(letter_p5_1) > 1:
            print(f"v1. The first index of the letter \"{letter_p5_1}\" "
                  f"in the string is [{str_p5_6.find(letter_p5_1)}] "
                  f"and last index is [{str_p5_6.rfind(letter_p5_1)}]"
                  f"==================\n"
                  f"v2. The first index of the letter \"{letter_p5_1}\" "
                  f"in the string is [{str_p5_6.index(letter_p5_1)}] "
                  f"and last index is [{str_p5_6.rindex(letter_p5_1)}]")
        else:
            print(f"v1. The index of the letter \"{letter_p5_1}\" in the string is [{str_p5_6.index(letter_p5_1)}]")
            print(f"v2. The index of the letter \"{letter_p5_1}\" in the string is [{str_p5_6.find(letter_p5_1)}]")
    else:
        print(f"The letter \"{letter_p5_1}\" not in the string")

letter_p5_1 = "f"
str_p5_6 = """Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс. 
              Если f встречается два и более раз, выведите индекс ее первого и последнего появления. 
              Если буква f в данной строке не встречается, ничего не выводите. 
              При решении этой задачи не стоит использовать циклы."""

index_letter_in_str_p5_6(str_p5_6, letter_p5_1)