
from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('Aquarium name cannot be an empty string.')
        self.__name = value

    def calculate_comfort(self):
        return sum([el.comfort for el in self.decorations])

    def add_fish(self,fish):
        if self.capacity > 0:
            self.fish.append(fish)
            self.capacity -= 1
            return f'Successfully added {fish.__class__.name} to {self.name}.'
        else:
            'Not enough capacity.'

    def remove_fish(self, fish):
        self.fish.remove(fish)
        self.capacity += 1

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = ''
        if len(self.fish) > 0:
            result += f"{self.name}:\nFish: {' '.join([el.name for el in self.fish])}\n" \
                      f"Decorations: {len(self.decorations)}\nComfort: {self.calculate_comfort()}"
        else:
            result += f"{self.name}:\nFish: {'none'}\n" \
                      f"Decorations: {len(self.decorations)}\nComfort: {self.calculate_comfort}"
        return result




# b = BaseAquarium('v', 10)
# print(b.__dict__)