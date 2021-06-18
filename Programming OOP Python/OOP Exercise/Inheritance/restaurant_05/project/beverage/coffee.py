# from Inheritance.restaurant_05.project.beverage.hot_beverage import HotBeverage
from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    COFFEE_MILLILITERS = 50
    COFFEE_PRICE = 3.50

    def __init__(self, name, caffeine):
        HotBeverage.__init__(self, name, Coffee.COFFEE_PRICE, Coffee.COFFEE_MILLILITERS)
        self._caffeine = caffeine

    @property
    def caffeine(self):
        return self._caffeine
