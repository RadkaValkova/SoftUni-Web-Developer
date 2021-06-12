# from Exercises2.players_and_monsters2.project.dark_knight import DarkKnight
from project.dark_knight import DarkKnight


class BladeKnight(DarkKnight):
    def __init__(self, username, level):
        super().__init__(username, level)