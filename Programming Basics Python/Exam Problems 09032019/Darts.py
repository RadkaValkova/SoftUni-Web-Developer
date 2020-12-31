player_name = input()
bad_shots = 0
good_shots = 0
current_points = 301
while True:
    field = input()
    if field == 'Retire':
        print(f'{player_name} retired after {bad_shots} unsuccessful shots.')
        break
    current_shot = int(input())

    if field == 'Single':
        current_shot = current_shot
    elif field == 'Double':
        current_shot = (current_shot * 2)
    elif field == 'Triple':
        current_shot = (current_shot * 3)

    if current_points > current_shot:
        good_shots += 1
        current_points -= current_shot
    elif current_points < current_shot:
        bad_shots += 1
        current_points = current_points
    elif current_points == current_shot:
        good_shots += 1
        current_points -= current_shot
        print(f'{player_name} won the leg with {good_shots} shots.')
        break

