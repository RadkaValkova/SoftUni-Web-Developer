days = int(input())
available_food = float(input())

day_dog_food = 0
all_dog_food = 0
day_cat_food = 0
all_cat_food = 0
biscuits = 0
total_eaten_food = 0

for current_day in range(1, days+1):
    day_dog_food = int(input())
    all_dog_food += day_dog_food
    day_cat_food = int(input())
    all_cat_food += day_cat_food
    total_eaten_food = all_dog_food + all_cat_food
    if current_day % 3 == 0:
        biscuits += ((day_dog_food+day_cat_food) * 0.1)

print(f'Total eaten biscuits: {round(biscuits)}gr.')
print(f'{(total_eaten_food/available_food*100):.2f}% of the food has been eaten.')
print(f'{(all_dog_food/total_eaten_food*100):.2f}% eaten from the dog.')
print(f'{(all_cat_food/total_eaten_food*100):.2f}% eaten from the cat.')



