"""
n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок
достанется каждому школьнику? Сколько яблок останется в корзинке? Программа получает на
вход числа n и k и должна вывести искомое количество яблок (два числа).
"""


def apple_per_schoolchildren():
    n = int(input("schoolchildren: "))
    k = int(input("apples: "))

    apple = k // n
    basket = k % n
    print(f"Apple per schoolchildren {apple} and {basket} in the basket")


#apple_per_schoolchildren()


def operations():
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    n3 = int(input("n3: "))
    n4 = int(input("n4: "))
    fun = input("Type name function: ")
    SEC_IN_MIN = 60

    def print_res():
        print(f"Result of {fun} by numbers {n1}, {n2}, {n3}, {n4} = {res}")

    if fun == "sum":
        res = sum([n1, n2, n3, n4])
        print_res()
    elif fun == "multiply":
        res = n1 * n2 * n3 * n4
        print_res()
    elif fun == "sec":
        res = n1 * 24 * SEC_IN_MIN * 2 + n2 * SEC_IN_MIN * 2  + n3 * SEC_IN_MIN + n4
        print_res()

operations()
