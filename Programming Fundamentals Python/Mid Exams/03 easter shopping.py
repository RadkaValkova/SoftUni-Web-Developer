shops = input().split()
number_of_commands = int(input())

for i in range(number_of_commands):
    line = input().split()
    command = line[0]
    if command == 'Include':
        shop = line[1]
        shops.append(shop)

    elif command == 'Visit':
        direction = line[1]
        number = int(line[2])
        if direction == 'first' and number <= len(shops):
            for y in range(number):
                shops.remove(shops[0])
        elif direction == 'last' and number <= len(shops):
            for z in range(number):
                shops.remove(shops[-1])

    elif command == 'Prefer':
        index_1 = int(line[1])
        index_2 = int(line[2])
        if index_1 in range(len(shops)) and index_2 in range(len(shops)):
            shops[index_1], shops[index_2] = shops[index_2], shops[index_1]

    elif command == 'Place':
        shop = line[1]
        index = int(line[2])+1
        if index in range(len(shops)):
            shops.insert(index, shop)

print('Shops left:')
print(' '.join(shops))
