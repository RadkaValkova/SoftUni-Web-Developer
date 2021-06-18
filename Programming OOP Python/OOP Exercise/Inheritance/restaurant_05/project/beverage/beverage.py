# from Inheritance.restaurant_05.project.product import Product
from project.product import Product


class Beverage(Product):
    def __init__(self, name, price, milliliters):
        Product.__init__(self, name, price)
        self._milliliters = milliliters

    @property
    def milliliters(self):
        return self._milliliters
