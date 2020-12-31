names = input().split(', ')
blacklisted_count = 0
lost_count = 0
line = input()

while line != 'Report':
    tokens = line.split()
    command = tokens[0]

    if command == 'Blacklist':
        name = tokens[1]
        if name not in names:
            print(f'{name} was not found.')
        else:
            names[names.index(name)] = 'Blacklisted'
            blacklisted_count += 1
            print(f'{name} was blacklisted.')

    elif command == 'Error':
        index = int(tokens[1])
        if names[index] != 'Blacklisted' and names[index] != 'Lost':
            print(f'{names[index]} was lost due to an error.')
            names[index] = 'Lost'
            lost_count += 1

    elif command == 'Change':
        index = int(tokens[1])
        new_name = tokens[2]
        if index in range(len(names)):
            print(f'{names[index]} changed his username to {new_name}.')
            names[index] = new_name
    line = input()

print(f'Blacklisted names: {blacklisted_count}')
print(f'Lost names: {lost_count}')
print(' '.join(names))