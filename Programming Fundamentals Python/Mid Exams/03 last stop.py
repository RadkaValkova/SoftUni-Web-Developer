numbers = input().split()
numbers_int = list(map(int, numbers))

while True:
    line = input()
    if line == 'END':
        break
    command = line.split()[0]
    if command == 'Change':
        old_num = int(line.split()[1])
        new_num = int(line.split()[2])
        if old_num in numbers_int:
            numbers_int[numbers_int.index(old_num)] = new_num

    elif command == 'Hide':
        num_to_hide = int(line.split()[1])
        if num_to_hide in numbers_int:
            numbers_int.remove(num_to_hide)

    elif command == 'Switch':
        first_num = int(line.split()[1])
        second_num = int(line.split()[2])
        if first_num in numbers_int and second_num in numbers_int:
            index1 = numbers_int.index(first_num)
            index2 = numbers_int.index(second_num)
            numbers_int[index1], numbers_int[index2] = numbers_int[index2], numbers_int[index1]

    elif command == 'Insert':
        index = int(line.split()[1])
        num_to_insert = int(line.split()[2])
        if index in range(len(numbers_int)):
            numbers_int.insert(index+1,num_to_insert)

    elif command == 'Reverse':
        numbers_int = numbers_int[::-1]

print(*numbers_int)