"""Создайте класс Animal с методами eat() и run().
Наследуйте от него классы Cat и класс Dog.
Эти классы должны иметь
 - атрибут name
 - и методы eat() и run().
При вызове методов eat() и run() соответственно выводится на печать:
"Кот Рыжик ест"
"Кот Рыжик бегает"
"Собака Шарик ест"
"Собака Шарик бегает"
"""


class Animal:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def translate_cn(class_name):
        translations = {"Cat": "Кот", "Dog": "Собака", "Fish": "Рыба"}
        return translations.get(class_name, class_name)

    def eat(self):
        print(f"{self.translate_cn(self.__class__.__name__)} {self.name} ест")

    def run(self):
        print(f"{self.translate_cn(self.__class__.__name__)} {self.name} бегает")


class Cat(Animal):
    def eat(self):
        print(f"{self.translate_cn(self.__class__.__name__)} {self.name} плохо ест")


class Dog(Animal):
    def run(self):
        print(f"{self.translate_cn(self.__class__.__name__)} {self.name} хорошо бегает")

class Fish(Animal):
    pass


# Кот Рыжик ест.
# Кот Рыжик бегает.
# Собака Шарик ест.
# Собака Шарик бегает.

if __name__ == "__main__":
    cat_ryzhik = Cat("Рыжик")
    dog_sharik = Dog("Шарик")

    cat_ryzhik.eat()
    cat_ryzhik.run()
    dog_sharik.eat()
    dog_sharik.run()
