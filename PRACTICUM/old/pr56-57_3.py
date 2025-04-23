class Person:
    def __init__(self, name, age, gender="Undefined"):
        self.name = name
        self.age = age
        self.gender = gender


class Student(Person):
    def __init__(self, name, age, group, gender="Undefined"):
        super().__init__(name, age, gender)
        self.group = group


p1 = Person("Ivan", 20)
students = [
    {"name": "Peter", "age": 25, "group": "A", "gender": "Male"},
    {"name": "John", "age": 22, "group": "B"},
    {"name": "Alice", "age": 23, "group": "C"},
]

student_objects = [Student(**student) for student in students]
print(p1.name, p1.age)
for student in student_objects:
    print(f"Name: {student.name}, Age: {student.age}, Group: {student.group}, Gender: {student.gender}")
print(p1.__dict__)
print([student.__dict__ for student in student_objects])
