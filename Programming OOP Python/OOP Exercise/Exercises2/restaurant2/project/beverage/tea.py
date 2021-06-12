# from Exercises2.restaurant2.project.beverage.hot_beverage import HotBeverage
from project.beverage.hot_beverage import HotBeverage


class Tea(HotBeverage):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)