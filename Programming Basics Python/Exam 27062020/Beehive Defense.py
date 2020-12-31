bees_number = int(input())
bear_health = int(input())
bear_attacks_power = int(input())

while True:
    bees_number -= bear_attacks_power
    bear_health -= (bees_number * 5)
    if bees_number < 100:
        if bees_number < 0:
            bees_number = 0
        print(f'The bear stole the honey! Bees left {bees_number}.')
        break
    if bear_health <= 0:
        if bees_number < 0:
            bees_number = 0
        print(f'Beehive won! Bees left {bees_number}.')
        break
