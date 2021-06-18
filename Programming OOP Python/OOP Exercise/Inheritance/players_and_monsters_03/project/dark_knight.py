# from Inheritance.players_and_monsters_03.project.knight import Knight
from project.knight import Knight

class DarkKnight(Knight):
    class_name = 'DarkKnight'

    def __init__(self, username, level):
        super().__init__(username, level)