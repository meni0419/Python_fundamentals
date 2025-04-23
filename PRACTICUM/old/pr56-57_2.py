class Person:
    def __init__(self, name, age, gender="Undefined"):
        self.name = name
        self.age = age
        self.gender = gender

class Student(Person):
    def __init__(self, name, age, group, gender):
        super().__init__(name, age, gender)
        self.group = group

p1 = Person("Ivan", 20)
s1 = Student("Peter", 25, "A", "male")
print(f"Person: {p1.name}, {p1.age}, {p1.gender}")
print(f"Student: {s1.name}, {s1.age}, {s1.group}, {s1.gender}")
