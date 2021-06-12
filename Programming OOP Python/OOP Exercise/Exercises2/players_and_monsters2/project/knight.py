# from Exercises2.players_and_monsters2.project.hero import Hero
from project.hero import Hero


class Knight(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)