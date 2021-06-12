# from Exercises2.restaurant2.project.food.main_dish import MainDish
from project.food.main_dish import MainDish


class Salmon(MainDish):
    def __init__(self, name, price, grams):
        super().__init__(name, price, grams=22)