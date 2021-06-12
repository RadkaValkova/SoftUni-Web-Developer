# from Exercises2.players_and_monsters2.project.elf import Elf
from project.elf import Elf


class MuseElf(Elf):
    def __init__(self, username, level):
        super().__init__(username, level)