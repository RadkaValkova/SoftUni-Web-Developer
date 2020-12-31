gifts = input().split()

line = input()

while line != 'No Money':
    command = line.split()[0]
    if command == 'OutOfStock':
        gift = line.split()[1]
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = 'None'

    elif command == 'Required':
        gift = line.split()[1]
        index = int(line.split()[2])
        if index in range(len(gifts)):
            gifts[index] = gift

    elif command == 'JustInCase':
        gift = line.split()[1]
        gifts[-1] = gift

    line = input()

print(' '.join([el for el in gifts if el != 'None']))