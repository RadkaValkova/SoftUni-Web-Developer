# from Inheritance.players_and_monsters_03.project.elf import Elf
from project.elf import Elf

class MuseElf(Elf):
    class_name = 'MuseElf'

    def __init__(self, username, level):
        super().__init__(username, level)