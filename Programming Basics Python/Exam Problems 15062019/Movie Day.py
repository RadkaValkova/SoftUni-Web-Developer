time_for_shoot = int(input())
scenes_number = int(input())
scenes_time = int(input())

preparation = time_for_shoot * 0.15
total_time_needed = preparation + scenes_number*scenes_time

if total_time_needed <= time_for_shoot:
    print(f'You managed to finish the movie on time! You have {(time_for_shoot-total_time_needed):.0f} minutes left!')
else:
    print(f'Time is up! To complete the movie you need {(total_time_needed-time_for_shoot):.0f} minutes.')