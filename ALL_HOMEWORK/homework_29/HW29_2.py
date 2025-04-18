"""
Создайте класс Student для представления студента.
Класс должен иметь атрибуты name (имя) и age (возраст),
а также метод display_info(), который выводит информацию о студенте.
Затем создайте экземпляр класса Student с заданным именем и возрастом и вызовите метод display_info()."""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return self.name, self.age


student_petrov = Student("Petrov", 20)

print(*list(student_petrov.display_info()))
print(student_petrov.name, student_petrov.age)


class Student_v2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"{self.name} {self.age}")


student_shchegol = Student_v2("Shchegol", 10)
student_shchegol.display_info()