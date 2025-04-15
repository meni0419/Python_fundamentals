""" 04-05 ==========================================================
Создать класс Person с полями имя и дата рождения (формат str).
Создать класс Employee который содержит поле имя и возраст (int)


Создать 10 объектов класса Person с разными именами.

Написать функцию, которая
    из списка объекта класса Person старше 18 лет
    создаёт список из объектов класса Employee,
    вычисляя возраст каждого Person по дате рождения.

Используя map и filter, попробуйте реализовать трансформации 
списка Person в список Employee в одну строчку.

Вывести получившихся сотрудников на экран.

Используя функцию all() убедиться, что все сотрудники действительно старше 18 лет.
"""
from datetime import datetime


class Person:
    def __init__(self, name: str, birth_day: str):
        self.name = name
        self.birth_day = birth_day

    def get_age(self):
        birthdate = datetime.strptime(self.birth_day, '%Y-%m-%d').date()
        today = datetime.today().date()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age


class Employee:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


"""
# Alternative solution with map and filter

def get_employee_list(person_list: list) -> list:
    return list(map(lambda person: Employee(person.name, person.get_age()),
                    filter(lambda person: person.get_age() > 18, person_list)))


employees = get_employee_list(list_of_persons)
"""

list_of_persons = [
    Person("Alice", "2000-06-15"),
    Person("Bob", "2010-03-22"),
    Person("Charlie", "1995-12-30"),
    Person("Diana", "2015-07-19"),
    Person("Ethan", "1990-11-02"),
    Person("Fiona", "2013-01-25"),
    Person("George", "1999-09-13"),
    Person("Hannah", "2002-04-08"),
    Person("Ian", "1988-08-31"),
    Person("Jenny", "1993-05-06"),
]

employees = [Employee(person.name, person.get_age()) for person in list_of_persons if person.get_age() > 18]

# Print the list of Employee objects
print("\033[1m\033[32m"
      "List of Employee objects:\033[0m")
for employee in employees:
    print(f"{employee.name}, {employee.age}")
print(f"================\n"
      f"all(employees) >= 18: \033[1m\033[32m{all(employee.age > 18 for employee in employees)}\033[0m")
