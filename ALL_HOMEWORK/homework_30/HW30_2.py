"""
Создайте класс BankAccount для представления банковского счета.
Класс должен иметь атрибуты account_number (номер счета) и balance (баланс),
а также методы deposit() для внесения денег на счет и withdraw() для снятия денег со счета.
Затем создайте экземпляр класса BankAccount, внесите на счет некоторую сумму и снимите часть денег.
Выведите оставшийся баланс. Не забудьте предусмотреть вариант, при котором при снятии баланс может стать меньше нуля.
В этом случае уходить в минус не будем, вместо чего будем возвращать сообщение "Недостаточно средств на счете"."""

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance - amount < 0:
            return "Недостаточно средств на счете"
        else:
            self.balance -= amount
            return self.balance

my_bank_account = BankAccount(123456789, 500)

print(f"Current balance: ${my_bank_account.balance}")
print(f"After deposit +$100: ${my_bank_account.deposit(100)}")
print(f"After withdrawal -$50: ${my_bank_account.withdraw(50)}")
print(f"Final balance: ${my_bank_account.balance}")
print(f"After withdrawal -$1000: {my_bank_account.withdraw(1000)}")