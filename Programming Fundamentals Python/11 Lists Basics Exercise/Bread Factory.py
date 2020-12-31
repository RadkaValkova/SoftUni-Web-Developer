initial_energy = 100
initial_coins = 100

events = input().split('|')
is_bankrupt = False

for i in range(len(events)):
    tokens = events[i].split('-')
    command = tokens[0]
    value = int(tokens[1])

    if command == 'rest':
        initial_energy += value
        if initial_energy > 100:
            print(f'You gained {0} energy.')
            initial_energy = 100
        else:
            print(f'You gained {value} energy.')
        print(f'Current energy: {initial_energy}.')

    elif command == 'order':
        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += value
            print(f'You earned {value} coins.')
        elif initial_energy < 30:
            initial_energy += 50
            print('You had to rest!')

    else:
        initial_coins -= value
        if initial_coins > 0:
            print(f'You bought {command}.')
        else:
            print(f'Closed! Cannot afford {command}.')
            is_bancrupt = True
            break

if not is_bankrupt:
    print(f'Day completed!\nCoins: {initial_coins}\nEnergy: {initial_energy}')