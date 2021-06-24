from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, size=3, price=price)

    def eat(self):
        self.size += 3

# ff = FreshwaterFish('a', 'b', 10.1)
# print(ff.size)
# print(ff.__dict__)