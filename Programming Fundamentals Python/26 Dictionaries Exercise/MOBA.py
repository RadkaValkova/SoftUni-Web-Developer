players_pool = {}
while True:
    line = input()
    if line == 'Season end':
        break
    if '->' in line:
        tokens = line.split(' -> ')
        player = tokens[0]
        position = tokens[1]
        skill = int(tokens[2])
        if player not in players_pool:
            players_pool[player] = {position:0}
            if position in players_pool[player]:
                if players_pool[player][position] < skill:
                    players_pool[player][position] = skill
            else:
                players_pool[player][position] = skill
        else:
            if position in players_pool[player]:
                if players_pool[player][position] < skill:
                    players_pool[player][position] = skill
            else:
                players_pool[player][position] = skill

    elif 'vs' in line:
        tokens = line.split(' vs ')
        player1 = tokens[0]
        player2 = tokens[1]
        total_player1 = 0
        total_player2 = 0
        if player1 in players_pool and player2 in players_pool:
            for k,y in players_pool[player1].items():
                total_player1 += players_pool[player1][k]
            for k,y in players_pool[player2].items():
                total_player2 += players_pool[player2][k]

            # if total_player1 > total_player2:
            #     players_pool.pop(player2)
            # elif total_player1 < total_player2:
            #     players_pool.pop(player1)


print(players_pool)