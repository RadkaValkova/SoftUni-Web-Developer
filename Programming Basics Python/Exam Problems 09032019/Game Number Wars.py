player1 = input()
player2 = input()
points1 = 0
points2 = 0
is_winner_player1 = False
is_finished = False

for i in range(0,18):
    card_player1 = input()
    if card_player1 == 'End of game':
        is_finished = True
        break
    card_player2 = input()
    if int(card_player1) > int(card_player2):
        points1 += int(card_player1) - int(card_player2)
    elif int(card_player2) > int(card_player1):
        points2 += int(card_player2) - int(card_player1)
    elif int(card_player1) == int(card_player2):
        card_player1 = input()
        card_player2 = input()
        if int(card_player1) > int(card_player2):
            is_winner_player1 = True
            break
        elif int(card_player1) < int(card_player2):
            is_winner_player1 = False
            break

if is_finished:
    print(f'{player1} has {points1} points')
    print(f'{player2} has {points2} points')
elif is_winner_player1:
    print('Number wars!')
    print(f'{player1} is winner with {points1} points')
else:
    print('Number wars!')
    print(f'{player2} is winner with {points2} points')