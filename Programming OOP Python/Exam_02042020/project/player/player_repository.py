from project.player.beginner import Beginner
from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        if player not in self.players:
            self.players.append(player)
            self.count += 1
        else:
            raise ValueError(f'Player {player.username} already exists!')

    def remove(self,player: str):
        current = self.find(player)
        try:
            self.players.remove(current)
            self.count -= 1
        except ValueError:
            return 'Player cannot be an empty string!'

        # current = self.find(player)
        # if current:
        #     if current.username != '':
        #         self.players.remove(current)
        #         self.count -= 1
        #     else:
        #         raise ValueError('Player cannot be an empty string!')

    def find(self, username: str):
        for player in self.players:
            if player.username == username:
                return player


# a = Beginner('a')
# rep = PlayerRepository()
# print(rep.__dict__)
# print(rep.remove(''))