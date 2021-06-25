from project.supply.supply import Supply


class FoodSupply(Supply):
    def __init__(self):
        super().__init__(needs_increase=20)

    # @property
    # def needs_increase(self):
    #     return self.__needs_increase
    #
    # @needs_increase.setter
    # def needs_increase(self, value):
    #     if value < 0:
    #         raise ValueError('Needs increase cannot be less than zero.')
    #     self.__needs_increase = value
    #
    # def apply(self, survivor):
    #     survivor.needs += self.__needs_increase


# f = FoodSupply()
# print(f.__dict__)