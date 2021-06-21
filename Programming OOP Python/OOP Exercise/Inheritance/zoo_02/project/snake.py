# from Inheritance.zoo_02.project.reptile import Reptile
from project.reptile import Reptile


class Snake(Reptile):
    def __init__(self, name):
        Reptile.__init__(self, name)
