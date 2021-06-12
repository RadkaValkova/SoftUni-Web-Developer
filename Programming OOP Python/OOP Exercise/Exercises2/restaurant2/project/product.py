class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price


# product = Product("coffee", 2.5)
# print(product.__class__.__name__)
# print(product.name)
# print(product.price)
