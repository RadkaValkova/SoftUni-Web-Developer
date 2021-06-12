# from Exercises2.restaurant2.project.beverage.hot_beverage import HotBeverage
from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    def __init__(self, name, price, milliliters,caffeine):
        super().__init__(name, price=3.50, milliliters=50)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine


# c = Coffee('a', 1, 1, 1)
# print(c.name)
# print(c.price)
# print(c.milliliters)
# print(c.caffeine)
