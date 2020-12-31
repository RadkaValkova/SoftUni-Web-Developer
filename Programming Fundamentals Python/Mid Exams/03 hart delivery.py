houses = list(map(int, input().split('@')))

index = 0
while True:
    line = input()
    if line == 'Love!':
        break
    jump_length = int(line.split()[1])
    index += jump_length

    if index not in range(len(houses)):
        index = 0
    else:
        index = index

    if houses[index] > 0:
        houses[index] -= 2
        if houses[index] == 0:
            print(f'Place {index} has Valentine\'s day.')
    else:
        print(f'Place {index} already had Valentine\'s day.')

print(f'Cupid\'s last position was {index}.')
if sum(houses) == 0:
    print('Mission was successful.')
else:
    print(f'Cupid has failed {len([x for x in houses if x != 0])} places.')