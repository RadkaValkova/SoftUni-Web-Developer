# from Inheritance.players_and_monsters_03.project.hero import Hero
from project.hero import Hero


class Wizard(Hero):
    class_name = 'Wizard'

    def __init__(self, username, level):
        super().__init__(username, level)