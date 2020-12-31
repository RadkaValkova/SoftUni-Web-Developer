elements = list(map(int, input().split()))

while True:
    line = input()
    if line == 'end':
        break
    command = line.split()[0]

    if command == 'swap':
        index_1 = int(line.split()[1])
        index_2 = int(line.split()[2])
        elements[index_1], elements[index_2] = elements[index_2], elements[index_1]

    elif command == 'multiply':
        index_1 = int(line.split()[1])
        index_2 = int(line.split()[2])
        elements[index_1] = elements[index_1] * elements[index_2]

    elif command == 'decrease':
        elements = [el-1 for el in elements]

elements = list(map(str, elements))

print(', '.join(elements))
