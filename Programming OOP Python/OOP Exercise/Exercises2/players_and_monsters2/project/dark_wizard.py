# from Exercises2.players_and_monsters2.project.wizard import Wizard
from project.wizard import Wizard


class DarkWizard(Wizard):
    def __init__(self, username, level):
        super().__init__(username, level)
