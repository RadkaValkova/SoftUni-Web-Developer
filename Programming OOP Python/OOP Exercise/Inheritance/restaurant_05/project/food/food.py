# from Inheritance.restaurant_05.project.product import Product
from project.product import Product

class Food(Product):
    def __init__(self, name, price, grams):
        Product.__init__(self, name, price)
        self._grams = grams

    @property
    def grams(self):
        return self._grams
