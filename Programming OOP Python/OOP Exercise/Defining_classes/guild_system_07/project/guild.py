# from typing import List
# from guild_system_07.project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player.guild != self.name and player.guild != 'Unaffiliated':
            return f'Player {player.name} is in another guild.'
        elif player.guild == 'Unaffiliated' and player not in self.players:
            self.players.append(player)
            player.guild = self.name
            return f'Welcome player {player.name} to the guild {self.name}'
        elif player in self.players:
            return f'Player {player.name} is already in the guild.'

    def kick_player(self, player_name: str):
        player_list = [el for el in self.players if el.name == player_name]
        if player_list:
            current_player = player_list[0]
            self.players.remove(current_player)
            current_player.guild = 'Unaffiliated'
            return f'Player {current_player.name} has been removed from the guild.'
        else:
            return f'Player {player_name} is not in the guild.'

    def guild_info(self):
        result = f'Guild: {self.name}\n'
        for el in self.players:
            result += f'{el.player_info()}'
        return result


# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())

# player = Player("Pesho", 90, 90)
# player.add_skill("A", 3)
# print(player.player_info())
# expected = "Name: Pesho\nGuild: Unaffiliated\nHP: 90\nMP: 90\n===A - 3\n"

