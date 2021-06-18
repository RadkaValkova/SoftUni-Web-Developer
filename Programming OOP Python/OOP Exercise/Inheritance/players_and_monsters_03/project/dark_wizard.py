# from Inheritance.players_and_monsters_03.project.wizard import Wizard
from project.wizard import Wizard

class DarkWizard(Wizard):
    class_name = 'DarkWizard'

    def __init__(self, username, level):
        super().__init__(username, level)