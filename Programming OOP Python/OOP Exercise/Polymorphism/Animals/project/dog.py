# from Polymorphism.Animals.project.animal import Animal
from project.animal import Animal


class Dog(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def make_sound(self):
        return 'Woof!'

    def __repr__(self):
        return f'This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}'


# dog = Dog('tom', 15, 'male')
# print(dog.make_sound())
# print(dog.gender)
# print(repr(dog))