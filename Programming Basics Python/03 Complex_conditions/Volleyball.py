import math
year = input()
import math
year = input()
holidays = int(input())
trips = int(input())

games_in_Sofia = (48-trips)*3/4
games_at_home = trips
game_in_holidays = 2/3*holidays
total_games = games_in_Sofia + games_at_home + game_in_holidays

if year == 'leap':
    total_games = total_games * 1.15
else:
    total_games = total_games

print(math.floor(total_games))
