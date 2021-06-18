# from Inheritance.players_and_monsters_03.project.hero import Hero
from project.hero import Hero

class Elf(Hero):
    class_name = 'Elf'

    def __init__(self, username, level):
        super().__init__(username, level)