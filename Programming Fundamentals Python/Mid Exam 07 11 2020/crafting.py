particles = input().split('|')

line = input()

while line != 'Done':
    tokens = line.split()
    command = tokens[1]

    if command == 'Left':
        index = int(tokens[2])
        if index in range(len(particles)) and index - 1 >= 0:
            particles.insert(index-1, particles.pop(index))

    elif command == 'Right':
        index = int(tokens[2])
        if index in range(len(particles)):
            particles.insert(index + 2, particles[index])
            particles.pop(index)

    elif command == 'Even':
        even_elements = []
        for i in range(len(particles)):
            if i % 2 == 0:
                even_elements.append(particles[i])
        print(' '.join(even_elements))

    elif command == 'Odd':
        odd_elements = []
        for i in range(len(particles)):
            if i % 2 != 0:
                odd_elements.append(particles[i])
        print(' '.join(odd_elements))

    line = input()

print(f'You crafted {"".join(particles)}!')

