# from Exercises2.Wild_farm2.project.animals.animal import Bird
from project.animals.animal import Bird
# from Exercises2.Wild_farm2.project.food import Meat, Fruit, Vegetable
from project.food import Meat, Fruit, Vegetable


class Owl(Bird):
    def make_sound(self):
        return "Hoot Hoot"

    def feed(self,food):
        if not isinstance(food,Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        else:
            self.weight += 0.25* food.quantity
            self.food_eaten += food.quantity


class Hen(Bird):
    def make_sound(self):
        return "Cluck"

    def feed(self,food):
        self.weight += 0.35*food.quantity
        self.food_eaten += food.quantity




# owl = Owl("Pip", 10, 10)
# print(owl)
# meat = Meat(4)
# print(owl.make_sound())
# owl.feed(meat)
# veg = Vegetable(1)
# print(owl.feed(veg))
# print(owl)
