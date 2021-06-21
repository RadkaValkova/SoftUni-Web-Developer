# from Inheritance.zoo_02.project.animal import Animal
from project.animal import Animal

class Mammal(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
