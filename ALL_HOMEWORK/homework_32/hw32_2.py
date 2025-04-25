"""
Реализовать класс Email, представляющий электронное письмо. Класс должен поддерживать следующие операции:
- Сравнение писем по дате (операторы <, >, <=, >=, ==, !=)
- Преобразование письма в строку (метод __str__)
- Получение длины текста письма (метод __len__)
- Получение хеш-значения письма (метод __hash__)
- Проверка наличия текста в письме (метод __bool__)
"""


class Email:
    def __init__(self, from_, to, subject, text, date):
        self.from_ = from_
        self.to = to
        self.subject = subject
        self.text = text
        self.date = date

    def __str__(self):
        return (f"\033[1;34m{'=' * 50}\033[0m\n"
                f"\033[1;32mFrom:\033[0m {self.from_}\n"
                f"\033[1;32mTo:\033[0m {self.to}\n"
                f"\033[1;32mSubject:\033[0m {self.subject}\n"
                f"\033[1;33m{'-' * 50}\033[0m\n"
                f"{self.text}\n"
                f"\033[1;34m{'=' * 50}\033[0m")

    def __len__(self):
        return len(self.text)

    def len_text(self):
        return len(self.text)

    def __hash__(self):
        return hash((self.from_, self.to, self.subject, self.text, self.date))

    def __bool__(self):
        if self.text or self.subject:
            return True
        else:
            return False

    def __gt__(self, other):
        return self.date > other.date

    def __lt__(self, other):
        return self.date < other.date

    def __le__(self, other):
        return self.date <= other.date

    def __ge__(self, other):
        return self.date >= other.date

    def __eq__(self, other):
        return self.date == other.date

    def __ne__(self, other):
        return self.date != other.date


# Пример использования:
email1 = Email("john@example.com", "jane@example.com",
               "Meeting", "Hi Jane, let's have a meeting tomorrow.","2022-05-10")
email2 = Email("jane@example.com", "john@example.com",
               "Re: Meeting","Sure, let's meet at 2 PM.", "2022-05-10")
email3 = Email("alice@example.com", "bob@example.com",
               "Hello", "Hi Bob, how are you?", "2022-05-09")
email4 = Email("al@ex.com", "bob@ex.com",
               "", "", "2022-05-09")
print(email1)  # Вывод:

"""
From: john@example.com
To: jane@example.com
Subject: Meeting

Hi Jane, let's have a meeting tomorrow.
"""

print("Email2, Length:", len(email2))  # Вывод: 24
print("Email2, Text length:", email2.len_text())
print("Email3, Hash value:", hash(email3))  # Вывод: -920444056
print("Email1, Has text:", bool(email1))  # Вывод: True
print("Email4, has text:", bool(email4)) # Вывод: False
print("Email2, is later than email3:", email2 > email3)  # Вывод: True
