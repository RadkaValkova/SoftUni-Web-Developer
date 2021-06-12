# from Exercises2.restaurant2.project.product import Product
from project.product import Product


class Beverage(Product):
    def __init__(self, name, price,milliliters):
        super().__init__(name,price)
        self.__milliliters = milliliters

    @property
    def milliliters(self):
        return self.__milliliters


# beverage = Beverage("coffee", 2.5, 50)
# print(beverage.__class__.__name__)
# print(beverage.__class__.__bases__[0].__name__)
# print(beverage.name)
# print(beverage.price)
# print(beverage.milliliters)

