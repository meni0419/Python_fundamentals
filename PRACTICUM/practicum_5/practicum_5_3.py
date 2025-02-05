def count_words_p5_1(str_p5_3):
    """
    *Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов.
    Используйте для решения задачи метод count.
    """
    print(f"The number of words in the string is {str_p5_3.strip().count(' ') + 1}")
    print(f"The number of words in the string is {len(str_p5_3.strip().split(" "))}")

str_p5_3 = "Дана строка, состоящая из слов, разделенных пробелами."
count_words_p5_1(str_p5_3)
