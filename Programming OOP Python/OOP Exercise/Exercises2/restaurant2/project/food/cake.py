# from Exercises2.restaurant2.project.food.dessert import Dessert
from project.food.dessert import Dessert


class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name, price, grams, calories):
        super().__init__(name, price, grams, calories)
        self.price = self.PRICE
        self.grams = self.GRAMS
        self.calories = self.CALORIES
