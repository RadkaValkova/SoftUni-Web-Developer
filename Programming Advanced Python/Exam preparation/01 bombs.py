from collections import deque


def is_filled_pouch(ll,d,c,s):
    return ll[d] >= 3 and ll[c] >= 3 and ll[s] >= 3


bombs_info = {40: 'Datura', 60: 'Cherry', 120: 'Smoke Decoy'}
effects = deque(int(el) for el in input().split(', '))
casings = deque(int(el) for el in input().split(', '))
made_bombs = {'Datura': 0, 'Cherry': 0, 'Smoke Decoy': 0}

while True:
    if len(effects) <= 0 or len(casings) <= 0:
        break
    if is_filled_pouch(made_bombs, 'Datura', 'Cherry', 'Smoke Decoy'):
        break
    current_effect = effects[0]
    current_casing = casings[-1]
    if current_effect + current_casing in bombs_info:
        made_bombs[bombs_info[current_effect + current_casing]] += 1
        effects.popleft()
        casings.pop()
    else:
        casings[-1] -= 5

if is_filled_pouch(made_bombs,'Datura', 'Cherry', 'Smoke Decoy'):
    print('Bene! You have successfully filled the bomb pouch!')
else:
    print('You don\'t have enough materials to fill the bomb pouch.')

if effects:
    print(f'Bomb Effects: {", ".join(str(el) for el in effects)}')
else:
    print('Bomb Effects: empty')

if casings:
    print(f'Bomb Casings: {", ".join(str(el) for el in casings)}')
else:
    print('Bomb Casings: empty')

for k,v in sorted(made_bombs.items(), key= lambda x: x[0]):
    print(f'{k} Bombs: {v}')



