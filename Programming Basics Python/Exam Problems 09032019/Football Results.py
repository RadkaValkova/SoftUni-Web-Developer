win = 0
loos = 0
equal = 0
for i in range(1,3+1):
    game1 = input()
    if (game1[0]) > (game1[2]):
        win += 1
    elif (game1[0]) < (game1[2]):
        loos += 1
    elif (game1[0]) == (game1[2]):
        equal += 1
print(f'Team won {win} games.')
print(f'Team lost {loos} games.')
print(f'Drawn games: {equal}')
