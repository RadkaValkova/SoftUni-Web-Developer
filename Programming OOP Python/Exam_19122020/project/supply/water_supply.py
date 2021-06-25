from project.supply.supply import Supply


class WaterSupply(Supply):
    def __init__(self):
        super().__init__(needs_increase=40)

    # def apply(self, survivor):
    #     survivor.needs += self.__needs_increase


# w = WaterSupply()
# print(w.__dict__)