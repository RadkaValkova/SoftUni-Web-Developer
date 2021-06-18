# from Inheritance.players_and_monsters_03.project.dark_knight import DarkKnight
from project.dark_knight import DarkKnight

class BladeKnight(DarkKnight):
    class_name = 'BladeKnight'

    def __init__(self, username, level):
        super().__init__(username, level)