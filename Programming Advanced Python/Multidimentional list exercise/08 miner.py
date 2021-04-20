def get_matrix(n):
    matrix = []
    coals = 0
    start_position = (0, 0)
    for i in range(n):
        row = [el for el in input().split()]
        coals += row.count('c')
        matrix.append(row)
        if 's' in row:
            start_position = (i, row.index('s'))
    return matrix, coals, start_position


def get_moves(matrix, command, row,col):
    new_row = row
    new_col = col
    if command == 'up':
        new_row = row - 1
    elif command == 'right':
        new_col = col + 1
    elif command == 'left':
        new_col = col - 1
    elif command == 'down':
        new_row = row + 1
    if new_row in range(len(matrix)) and new_col in range(len(matrix[0])):
        return new_row, new_col
    else:
        return row,col


size = int(input())
commands = input().split()
matrix, coals, start_position = get_matrix(size)
start_row = start_position[0]
start_col = start_position[1]
not_collected = True

for i in range(len(commands)):
    current_command = commands[i]
    new_position = get_moves(matrix, current_command, start_row, start_col)
    if matrix[new_position[0]][new_position[1]] == 'c':
        coals -= 1
        matrix[new_position[0]][new_position[1]] = '*'
        if coals == 0:
            print(f'You collected all coals! ({new_position[0]}, {new_position[1]})')
            not_collected = False
            break
    elif matrix[new_position[0]][new_position[1]] == 'e':
        print(f'Game over! ({new_position[0]}, {new_position[1]})')
        not_collected = False
        break
    start_row = new_position[0]
    start_col = new_position[1]

if not_collected:
    print(f'{coals} coals left. ({start_row}, {start_col})')