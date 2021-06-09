# from Encapsulation.pizza_calories_02.project.dough import Dough
# from Encapsulation.pizza_calories_02.project.topping import Topping


class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.__toppings = {}

    @property
    def name(self):
        return self.__name

    @property
    def dough(self):
        return self.__dough

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @property
    def toppings(self):
        return self.__toppings

    @name.setter
    def name(self, value):
        self.__name = value

    @dough.setter
    def dough(self, value):
        self.__dough = value

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        self.__toppings_capacity = value

    @toppings.setter
    def toppings(self, value):
        self.__toppings = value

    def add_topping(self, topping):
        if self.__toppings_capacity > len(self.__toppings):
            if topping.topping_type not in self.__toppings:
                self.__toppings[topping.topping_type] = 0
            self.__toppings[topping.topping_type] += topping.weight
        else:
            raise ValueError('Not enough space for another topping')

    def calculate_total_weight(self):
        total_weight_toppings = sum([v for k, v in self.__toppings.items()])
        dough_weight = self.dough.weight
        return total_weight_toppings + dough_weight


# import unittest

# from project.dough import Dough
# from project.pizza import Pizza
# from project.topping import Topping


# class Tests(unittest.TestCase):
# def test_topping_init(self):
# t = Topping("Tomato", 20)
# print(t.topping_type, "Tomato")
# print(t.weight, 20)
#
# # def test_dough_init(self):
# d = Dough("Sugar", "Mixing", 20)
# print(d.flour_type, "Sugar")
# print(d.baking_technique, "Mixing")
# print(d.weight, 20)

# def test_pizza_init(self):
# d = Dough("Sugar", "Mixing", 20)
# p = Pizza("Burger", d, 5)
#
# print(p.name, "Burger")
# print(p.dough, d)
# print(len(p.toppings), 0)
# print(p.toppings_capacity, 5)

    # def test_pizza_add_topping_error(self):
    #     d = Dough("Sugar", "Mixing", 20)
    #     t = Topping("Tomato", 20)
    #     p = Pizza("Burger", d, 0)
    #     with self.assertRaises(ValueError) as ctx:
    #         p.add_topping(t)
    #     self.assertEqual("Not enough space for another topping", str(ctx.exception))

    # def test_pizza_add_topping_new(self):
    #     d = Dough("Sugar", "Mixing", 20)
    #     t = Topping("Tomato", 20)
    #     p = Pizza("Burger", d, 200)
    #     p.add_topping(t)
    #
    #     self.assertEqual(p.toppings["Tomato"], 20)
    #     self.assertEqual(len(p.toppings), 1)


# def test_pizza_add_topping_update(self):
# d = Dough("Sugar", "Mixing", 20)
# t = Topping("Tomato", 20)
# p = Pizza("Burger", d, 200)
# p.add_topping(t)
# p.add_topping(t)
#
# print(p.toppings["Tomato"], 40)

    # def test_pizza_calculate_total_weight(self):
# d = Dough("Sugar", "Mixing", 20)
# t = Topping("Tomato", 20)
# p = Pizza("Burger", d, 200)
# p.add_topping(t)
# p.add_topping(t)
#
# print(p.calculate_total_weight(), 60)

#
# if __name__ == '__main__':
#     unittest.main()
