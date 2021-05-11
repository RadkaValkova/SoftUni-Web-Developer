from collections import deque


def is_made(made_bombs):
    if made_bombs['Palm Fireworks'] >= 3 and made_bombs['Willow Fireworks'] >= 3 and made_bombs['Crossette Fireworks'] >= 3:
        return True
    else:
        return False


def removing_zeroes_and_less(ll):
    return [el for el in ll if el > 0]


effects = deque([int(x) for x in input().split(', ')])
explosive_power = [int(x) for x in input().split(', ')]

made_bombs = {'Palm Fireworks':0, 'Willow Fireworks': 0, 'Crossette Fireworks': 0}
is_collected = False

effects = deque(removing_zeroes_and_less(effects))
explosive_power = removing_zeroes_and_less(explosive_power)

while True:

    if not effects:
        break
    if not explosive_power:
        break

    first_effect = effects[0]
    last_explosive = explosive_power[-1]
    sum_elements = first_effect + last_explosive

    if sum_elements % 3 == 0 and sum_elements % 5 != 0:
        made_bombs['Palm Fireworks'] += 1
        effects.popleft()
        explosive_power.pop()
    elif sum_elements % 3 != 0 and sum_elements % 5 == 0:
        made_bombs['Willow Fireworks'] += 1
        effects.popleft()
        explosive_power.pop()
    elif sum_elements % 3 == 0 and sum_elements % 5 == 0:
        made_bombs['Crossette Fireworks'] += 1
        effects.popleft()
        explosive_power.pop()
    else:
        if effects[0] - 1 <= 0:
            effects.popleft()
        else:
            effects[0] -= 1
            effects.append(effects.popleft())

    if is_made(made_bombs):
        break


if made_bombs['Palm Fireworks'] >= 3 and made_bombs['Willow Fireworks'] >= 3 and made_bombs['Crossette Fireworks'] >= 3:
    print('Congrats! You made the perfect firework show!')
else:
    print('Sorry. You can’t make the perfect firework show.')

if effects:
    print(f'Firework Effects left: {", ".join([str(el) for el in effects])}')
if explosive_power:
    print(f'Explosive Power left: {", ".join([str(el) for el in explosive_power])}')

for k,v in made_bombs.items():
    print(f'{k}: {v}')



