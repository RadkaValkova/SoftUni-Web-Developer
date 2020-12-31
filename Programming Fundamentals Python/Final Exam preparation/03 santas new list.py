children = {}
presents = {}

while True:
    line = input()
    if line == 'END':
        break
    tokens = line.split('->')
    if tokens[0] != 'Remove':
        name = tokens[0]
        type_of_toy = tokens[1]
        amount = int(tokens[2])
        if name not in children:
            children[name] = amount
        else:
            children[name] += amount
        if type_of_toy not in presents:
            presents[type_of_toy] = amount
        else:
            presents[type_of_toy] += amount

    else:
        name = tokens[1]
        del children[name]

print('Children:')
for key,value in sorted(children.items(), key= lambda x: (-x[1], x[0])):
    print(f'{key} -> {value}')
print('Presents:')
for key,value in presents.items():
    print(f'{key} -> {value}')

