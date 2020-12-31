INITIAL_HEALTH = 100

commands = input().split('|')
total_health = INITIAL_HEALTH
total_bitcoins = 0
is_survived = True

for i in range(len(commands)):
    command, value = commands[i].split()
    if command == 'potion':
        current_health = int(value)
        difference = INITIAL_HEALTH - total_health
        total_health += current_health
        if total_health > INITIAL_HEALTH:
            total_health = INITIAL_HEALTH
            current_health = difference
        print(f'You healed for {current_health} hp.')
        print(f'Current health: {total_health} hp.')

    elif command == 'chest':
        total_bitcoins += int(value)
        print(f'You found {int(value)} bitcoins.')

    else:
        total_health -= int(value)
        if total_health <= 0:
            total_health = 0
            print(f'You died! Killed by {command}.')
            print(f'Best room: {i+1}')
            is_survived = False
            break
        else:
            print(f'You slayed {command}.')

if is_survived:
    print(f'You\'ve made it!\nBitcoins: {total_bitcoins}\nHealth: {total_health}')
