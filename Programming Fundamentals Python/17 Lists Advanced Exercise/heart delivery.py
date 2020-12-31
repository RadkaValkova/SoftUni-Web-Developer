neighborhood = list(map(int, (input().split('@'))))

command = input()
current_index = 0

while command != 'Love!':
    command_list = command.split()
    length = int(command_list[1])

    if current_index + length not in range(len(neighborhood)):
        current_index = 0
    else:
        current_index = (current_index + length) % len(neighborhood)

    if neighborhood[current_index] > 0:
        neighborhood[current_index] -= 2
        if neighborhood[current_index] == 0:
            print(f'Place {current_index} has Valentine\'s day.')
    else:
        print(f'Place {current_index} already had Valentine\'s day.')
    last_position = current_index
    command = input()

zeros = neighborhood.count(0)

print(f'Cupid\'s last position was {current_index}.')
if zeros == len(neighborhood):
    print('Mission was successful.')
else:
    print(f'Cupid has failed {len(neighborhood) - zeros} places.')