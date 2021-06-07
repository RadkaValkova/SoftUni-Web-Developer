# from typing import List
# from pokemon_battle_06.project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f'Caught {pokemon.pokemon_details()}'
        else:
            return 'This pokemon is already caught'

    def release_pokemon(self, pokemon_name:str):
        for el in self.pokemon:
            if el.name == pokemon_name:
                self.pokemon.remove(el)
                return f'You have released {pokemon_name}'
        if pokemon_name not in self.pokemon:
            return f'Pokemon is not caught'

    def trainer_data(self):
        result = f'Pokemon Trainer {self.name}\n'
        result += f'Pokemon count {len(self.pokemon)}\n'
        for el in self.pokemon:
            result += f'- {el.pokemon_details()}\n'
        return result


# pokemon = Pokemon("Pesho", 90)
# message = pokemon.pokemon_details()
# trainer = Trainer("Stamat")
# print(f"{trainer.name} 0")
# trainer = Trainer("Stamat")
# pokemon = Pokemon("Pesho", 90)
# print(trainer.add_pokemon(pokemon))
# trainer = Trainer("Stamat")
# pokemon = Pokemon("Pesho", 90)
# trainer.add_pokemon(pokemon)
# print(trainer.add_pokemon(pokemon))
# trainer = Trainer("Stamat")
# pokemon = Pokemon("Pesho", 90)
# trainer.add_pokemon(pokemon)
# print(trainer.release_pokemon("Pesho"))
# trainer = Trainer("Stamat")
# print(trainer.release_pokemon("Pesho"))
