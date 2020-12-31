targets = list(map(int, input().split()))

line = input()

while line != 'End':
    command_list = line.split()
    command = command_list[0]
    index = int(command_list[1])
    value = int(command_list[2])

    if command == 'Shoot':
        if index in range(len(targets)):
            if targets[index] > 0:
                targets[index] -= value
                if targets[index] <= 0:
                    targets.remove(targets[index])

    elif command == 'Add':
        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print('Invalid placement!')

    elif command == 'Strike':
        if index + value in range(len(targets)) and index - value in range(len(targets)):
            for i in range(index - value, index + value + 1):
                current_target = targets[i]
                targets.remove(current_target)
                targets.insert(i, 0)
        else:
            print('Strike missed!')

    line = input()

print('|'.join([str(x) for x in targets if x != 0]))