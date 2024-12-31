from decimal import Decimal, getcontext

getcontext().prec = 28
def sum_of_leibniz(n):
    i = Decimal('3')
    s_sum = Decimal('1')
    plus = False

    while n > 0:
        if plus:
            s_sum += Decimal('1') / i
            plus = False
        else:
            s_sum -= Decimal('1') / i
            plus = True
        i += Decimal('2')
        n -= 1

    return s_sum


num = int(input("Enter number: "))
print(f"Sum of first {num} Leibniz series: {sum_of_leibniz(num)}")
