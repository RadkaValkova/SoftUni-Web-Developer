team_name = input()
games = int(input())
points = 0
W = 0
D = 0
L = 0
if games < 1:
    print(f'{team_name} hasn\'t played any games during this season.')
else:
    for i in range(1, games+1):
        result = input()
        if result == 'W':
            points += 3
            W += 1
        elif result == 'D':
            points += 1
            D += 1
        else:
            points += 0
            L += 1

    print(f'{team_name} has won {points} points during this season.')
    print('Total stats:')
    print(f'## W: {W}')
    print(f'## D: {D}')
    print(f'## L: {L}')
    print(f'Win rate: {W/games*100:.2f}%')