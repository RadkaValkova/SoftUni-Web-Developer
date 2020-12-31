class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.mammals = []
        self.fish = []
        self.birds = []
        self.zoo_name = zoo_name

    def add_animal(self, species, animal):
        if species == 'mammal':
            self.mammals.append(animal)
        elif species == 'fish':
            self.fish.append(animal)
        elif species == 'bird':
            self.birds.append(animal)
        Zoo.__animals += 1

    def get_info(self, species):
        current = []
        if species == 'mammal':
            current = self.mammals
            print(f'{species.capitalize()}s in {self.zoo_name}: {", ".join(current)}')
        elif species == 'fish':
            current = self.fish
            print(f'Fishes in {self.zoo_name}: {", ".join(current)}')
        elif species == 'bird':
            current = self.birds
            print(f'{species.capitalize()}s in {self.zoo_name}: {", ".join(current)}')
        print(f'Total animals: {Zoo.__animals}')


zoo = Zoo(input())

n = int(input())
for i in range(n):
    line = input()
    species, animal = line.split()
    zoo.add_animal(species, animal)

species = input()

zoo.get_info(species)
