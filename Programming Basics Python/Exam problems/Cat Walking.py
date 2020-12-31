minutes_for_day = int(input())
walks_for_day = int(input())
eated_calories_for_day = int(input())

burned_calories_for_day = minutes_for_day * walks_for_day * 5
if burned_calories_for_day >= eated_calories_for_day/2:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {burned_calories_for_day}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {burned_calories_for_day}.')
