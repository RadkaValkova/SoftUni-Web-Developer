days = int(input())
players = int(input())
groups_energy = float(input())
day_water_per_person = float(input())
day_food_per_person = float(input())
total_water = days * players * day_water_per_person
total_food = days * players * day_food_per_person
is_enough_energy = True

for i in range(1, days+1):
    energy_loss = float(input())
    groups_energy -= energy_loss
    if groups_energy <= 0:
        is_enough_energy = False
        break
    if i % 2 == 0:
        groups_energy += groups_energy * 0.05
        total_water -= total_water * 0.30
    if i % 3 == 0:
        total_food -= total_food/players
        groups_energy += groups_energy * 0.10

if is_enough_energy:
    print(f'You are ready for the quest. You will be left with - {groups_energy:.2f} energy!')
else:
    print(f'You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.')

