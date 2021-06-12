# from Exercises2.restaurant2.project.food.starter import Starter
from project.food.starter import Starter


class Soup(Starter):
    def __init__(self, name, price, grams):
        super().__init__(name, price, grams)


# soup = Soup("fish soup", 9.90, 230)
# print(soup.__class__.__name__)
# print(soup.__class__.__bases__[0].__name__)
# print(soup.name)
# print(soup.price)
# print(soup.grams)
