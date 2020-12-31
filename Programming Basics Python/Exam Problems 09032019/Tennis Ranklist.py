import math
tournament = int(input())
start_points = int(input())
tournament_count = 0
w_counter = 0
sum_ponts = start_points

while True:
    stage = input()
    tournament_count += 1

    if stage == 'W':
        w_counter += 1
        sum_ponts += 2000
    elif stage == 'F':
        sum_ponts += 1200
    elif stage == 'SF':
        sum_ponts += 720
    if tournament == tournament_count:
        break
print(f'Final points: {sum_ponts}')
print(f'Average points: {math.floor((sum_ponts-start_points)/tournament_count)}')
print(f'{(w_counter/tournament_count*100):.2f}%')