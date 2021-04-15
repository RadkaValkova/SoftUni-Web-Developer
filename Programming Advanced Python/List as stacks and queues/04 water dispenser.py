from collections import deque

water = int(input())

people = deque()

line = input()
while line != 'Start':
    people.append(line)
    line = input()

while True:
    line = input()
    if line == 'End':
        print(f'{water} liters left')
        break
    tokens = line.split(' ')
    if tokens[0] == 'refill':
        water += int(tokens[1])
    else:
        needed_water = int(tokens[0])
        if water >= needed_water:
            water -= needed_water
            print(f'{people.popleft()} got water')
        else:
            print(f'{people.popleft()} must wait')

