# animal_sounds = {'cat': 'meow','dog': 'woof-woof'}
#
# class Animal:
#     def __init__(self, species):
#         self.species = species
#
#     def get_species(self):
#         return self.species
#
#
# def animal_sound(animals: list):
#     for animal in animals:
#         try:
#             print(animal_sounds[animal.get_species()])
#         except:
#             print('Unknown sound')
#
#
# animals = [Animal('cat'), Animal('dog')]
# animal_sound(animals)
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def make_sound(self):
        return


class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.sound = 'meow'

    def make_sound(self):
        return self.sound


