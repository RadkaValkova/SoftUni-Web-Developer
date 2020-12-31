targets = list(map(int, input().split('|')))
points = 0
line = input()

while line != 'Game over':
    command = line.split('@')[0]
    if command == 'Shoot Left':
        start_index = int(line.split('@')[1])
        length = int(line.split('@')[2])
        target_index = (start_index - length) % len(targets)
        if start_index in range(len(targets)):
            if targets[target_index] >= 5:
                targets[target_index] -= 5
                points += 5
            else:
                points += targets[target_index]
                targets[target_index] = 0

    elif command == 'Shoot Right':
        start_index = int(line.split('@')[1])
        length = int(line.split('@')[2])
        target_index = (start_index + length) % len(targets)
        if start_index in range(len(targets)):
            if targets[target_index] >= 5:
                targets[target_index] -= 5
                points += 5
            else:
                points += targets[target_index]
                targets[target_index] = 0

    elif command == 'Reverse':
        targets = targets[::-1]

    line = input()

print(' - '.join([str(el) for el in targets]))
print(f'Iskren finished the archery tournament with {points} points!')