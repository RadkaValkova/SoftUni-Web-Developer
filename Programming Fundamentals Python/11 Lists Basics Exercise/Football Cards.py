cards = input().split()
team_a = []
team_b = []
counter_team_a = 11
counter_team_b = 11
game_is_over = False                                   #Тук първо разбиваме листа на отделни играчи, \
                                                        # а после разбиваме всеки играч на отбор и номер

for card in cards:
    tokens = card.split('-')
    team = tokens[0]
    player_number = int(tokens[1])
    if counter_team_a < 7 or counter_team_b < 7:
        game_is_over = True
        break
    if team == 'A':
        if player_number not in team_a:
            team_a.append(player_number)
            counter_team_a -= 1
        else:
            continue
    else:
        if player_number not in team_b:
            team_b.append(player_number)
            counter_team_b -= 1
        else:
            continue
print(f'Team A - {counter_team_a}; Team B - {counter_team_b}')
if game_is_over:
    print('Game was terminated')

# cards = input()
# cards_list = cards.split(' ')
#
# send_off_team_A = []
# send_off_team_B = []
# game_is_over = False
#
# for i in range(len(cards_list)):
#     current_card = cards_list[i].split('-')
#     if current_card[0] == 'A':
#         if current_card[1] in send_off_team_A:
#             continue
#         else:
#             send_off_team_A.append(current_card[1])
#     else:
#         if current_card[1] in send_off_team_B:
#             continue
#         else:
#             send_off_team_B.append(current_card[1])
#     if (11 - len(send_off_team_A)) < 7 or (11 - len(send_off_team_B)) < 7:
#         game_is_over = True
#         break
#
# print(f'Team A - {11 - len(send_off_team_A)}; Team B - {11 - len(send_off_team_B)}')
# if game_is_over:
#     print('Game was terminated')