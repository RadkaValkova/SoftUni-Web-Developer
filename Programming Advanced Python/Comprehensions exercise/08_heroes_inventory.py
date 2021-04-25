# heroes_names = input().split(', ')

# heroes = {}
# for name in heroes_names:
#     if name not in heroes:
#         heroes[name] = [[], []]

heroes = {name:[[], []] for name in input().split(', ')}

while True:
    line = input()
    if line == 'End':
        break
    tokens = line.split('-')
    name = tokens[0]
    item = tokens[1]
    cost = int(tokens[2])

    if item not in heroes[name][0]:
        heroes[name][0].append(item)
        heroes[name][1].append(cost)

[print(f'{key} -> Items: {len(heroes[key][0])}, Cost: {sum(heroes[key][1])}') for key,value in heroes.items()]

