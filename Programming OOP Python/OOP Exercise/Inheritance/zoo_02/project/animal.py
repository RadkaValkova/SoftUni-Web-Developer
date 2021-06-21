# from Inheritance.zoo_02.project.lizard import Lizard
# from Inheritance.zoo_02.project.mammal import Mammal
# from project.lizard import Lizard
# from project.mammal import Mammal

class Animal:
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name


# mammal = Mammal("Stella")
# print(mammal.__class__.__bases__[0].__name__)
# print(mammal.name)
# print(mammal._Animal__name)
# lizard = Lizard("John")
# print(lizard.__class__.__bases__[0].__name__)
# print(lizard.name)
# print(lizard._Animal__name)


