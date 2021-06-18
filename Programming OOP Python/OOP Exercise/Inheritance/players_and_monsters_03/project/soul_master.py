# from Inheritance.players_and_monsters_03.project.dark_wizard import DarkWizard
from project.dark_wizard import DarkWizard


class SoulMaster(DarkWizard):
    class_name = 'SoulMaster'

    def __init__(self, username, level):
        super().__init__(username, level)