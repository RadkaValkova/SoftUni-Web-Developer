from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant

class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == 'FreshwaterAquarium':
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
            return f'Successfully added {aquarium_type}.'
        elif aquarium_type == 'SaltwaterAquarium':
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
            return f'Successfully added {aquarium_type}.'
        else:
            return 'Invalid aquarium type.'

    def add_decoration(self, decoration_type: str):
        if decoration_type == 'Ornament':
            self.decorations_repository.decorations.append(Ornament())
            return f'Successfully added {decoration_type}.'
        elif decoration_type == 'Plant':
            self.decorations_repository.decorations.append(Plant())
            return f'Successfully added {decoration_type}.'
        else:
            return 'Invalid decoration type.'

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        pass

    def add_fish(self,aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        pass

    def feed_fish(self, aquarium_name: str):
        current = [el for el in self.aquariums if el.name == aquarium_name]
        for el in current:
            el.eat()
            return f'Fish fed: {len(current)}'

    def calculate_value(self, aquarium_name: str):
        current = [el for el in self.aquariums if el.name == aquarium_name][0]
        result = current.calculate_comfort() + [el.price for el in current.decorations] + [el.price for el in current.fish]
        return result

    def report(self):
        pass


