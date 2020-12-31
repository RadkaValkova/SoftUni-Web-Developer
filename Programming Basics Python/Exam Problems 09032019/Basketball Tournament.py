win_counter = 0
loos_counter = 0
game_count = 0

while True:
    tournament = input()
    if tournament == 'End of tournaments':
        print(f'{(win_counter / game_count * 100):.2f}% matches win')
        print(f'{(loos_counter / game_count * 100):.2f}% matches lost')
        break

    game_number = int(input())
    game_count += game_number

    if tournament != 'End of tournaments':
        for i in range(1,game_number+1):
            point_Desi = int(input())
            point_others = int(input())

            if point_Desi > point_others:
                win_counter += 1
                print(f'Game {i} of tournament {tournament}: win with {point_Desi - point_others} points.')

            elif point_Desi < point_others:
                loos_counter += 1
                print(f'Game {i} of tournament {tournament}: lost with {point_others - point_Desi} points.')
