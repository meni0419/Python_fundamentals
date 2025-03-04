"""
4. Дано слово, состоящее только из строчных латинских букв. Проверьте, является ли это слово
палиндромом. Выведите YES или NO. Пример. is_palindrom(“radar”) вернет Yes,
is_palindrom(“yes”) вернет No.
"""


def is_palindrome(word, count=0):
    if word[count] != word[-count - 1]:
        return print("NO")
    elif count == len(word) - 1:
        return print("YES")
    is_palindrome(word, count + 1)


is_palindrome('radar')
