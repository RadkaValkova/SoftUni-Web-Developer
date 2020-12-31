initial_energy = int(input())

win_counter = 0
index = 1

while initial_energy >= 0:
    line = input()
    if line == 'End of battle':
        print(f'Won battles: {win_counter}. Energy left: {initial_energy}')
        break
    distance = int(line)
    if distance <= initial_energy:
        win_counter += 1
        if index % 3 == 0:
            initial_energy += win_counter
            initial_energy -= distance
        else:
            initial_energy -= distance
        index += 1
    else:
        print(f'Not enough energy! Game ends with {win_counter} won battles and {initial_energy} energy')
        break
