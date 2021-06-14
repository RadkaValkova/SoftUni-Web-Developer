# from Exercises2.Zoo2.project.animal import Animal
from project.animal import Animal

class Reptile(Animal):
    def __init__(self, name):
        super().__init__(name)