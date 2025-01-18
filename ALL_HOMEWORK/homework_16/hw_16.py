# ANSI escape codes for text colors
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"  # Resets the text color to default

print(
    f"""{BLUE}\n2. Напишите программу, которая принимает строку от пользователя и разбивает ее на отдельные слова. 
Затем программа должна создать новый кортеж, содержащий длину каждого слова в исходной строке. 
Используйте методы строк и кортежей для обработки данных.

Пример вывода:
{BLUE}Введите предложение: {GREEN}Программирование это интересно и полезно
{BLUE}Длины слов в предложении: {GREEN}(15, 3, 8, 2, 6) {RED}err: there is wrong count{RESET}""")


def word_lengths2():
    string = input("Введите предложение: ")
    words_length = tuple([len(word) for word in string.split()])
    print(f"Длины слов в предложении:{GREEN}{words_length}{RESET}")

