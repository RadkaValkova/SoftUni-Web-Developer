# from Exercises2.Wild_farm2.project.animals.animal import Mammal
from project.animals.animal import Mammal
# from Exercises2.Wild_farm2.project.food import Meat, Fruit, Vegetable
from project.food import Meat, Fruit, Vegetable


class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    def feed(self,food):
        if not isinstance(food,Vegetable) and not isinstance(food, Fruit):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        else:
            self.weight += 0.10*food.quantity
            self.food_eaten += food.quantity


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    def feed(self,food):
        if not isinstance(food,Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        else:
            self.weight += 0.40*food.quantity
            self.food_eaten += food.quantity


class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    def feed(self,food):
        if not isinstance(food,Meat) and not isinstance(food, Vegetable):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        else:
            self.weight += 0.30*food.quantity
            self.food_eaten += food.quantity


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def feed(self,food):
        if not isinstance(food,Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        else:
            self.weight += 1*food.quantity
            self.food_eaten += food.quantity


