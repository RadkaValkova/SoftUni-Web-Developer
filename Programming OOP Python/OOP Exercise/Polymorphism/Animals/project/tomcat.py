# from Polymorphism.Animals.project.cat import Cat
from project.cat import Cat


class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, gender='Male')

    def make_sound(self):
        return 'Hiss'

    # def __repr__(self):
    #     return f'This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}'


# tom = Tomcat('tom', 15)
# print(tom.make_sound())
# print(tom.gender)
# print(repr(tom))