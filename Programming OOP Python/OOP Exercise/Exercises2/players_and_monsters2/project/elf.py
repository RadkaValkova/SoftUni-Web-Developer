# from Exercises2.players_and_monsters2.project.hero import Hero
from project.hero import Hero


class Elf(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)


# elf = Elf("E", 4)
# print(str(elf))
# print(elf.__class__.__bases__[0].__name__)
# print(elf.username)
# print(elf.level)