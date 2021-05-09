def is_valid_position(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_out_of_matrix(command,row,col,size):
    new_r = 0
    new_c = 0
    if command == 'left':
        new_r,new_c = row,size-1
    elif command == 'right':
        new_r, new_c = row, 0
    elif command == 'down':
        new_r, new_c = 0,col
    elif command == 'up':
        new_r, new_c = size -1, col
    return new_r,new_c


size = int(input())
commands_number = int(input())
matrix = [list(input()) for _ in range(size)]
move_dict = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
start_coordinates = [(x, y) for x in range(0, size) for y in range(0, size) if matrix[x][y] == "f"]
start_row = start_coordinates[0][0]
start_col = start_coordinates[0][1]

is_won = False

for i in range(commands_number):
    command = input()
    current_row = start_row + move_dict[command][0]
    current_col = start_col + move_dict[command][1]
    if is_valid_position(current_row,current_col,size):
        if matrix[current_row][current_col] == 'B':
            matrix[start_row][start_col] = '-'
            current_row = current_row + move_dict[command][0]
            current_col = current_col + move_dict[command][1]
        elif matrix[current_row][current_col] == 'T':
            matrix[start_row][start_col] = '-'
            current_row = start_row
            current_col = start_col
        elif matrix[current_row][current_col] == 'F':
            matrix[start_row][start_col] = '-'
            matrix[current_row][current_col] = 'f'
            is_won = True
            break
        elif matrix[current_row][current_col] == '-':
            matrix[start_row][start_col] = '-'
            matrix[current_row][current_col] = 'f'
        start_row = current_row
        start_col = current_col
    else:
        matrix[start_row][start_col] = '-'
        start_row, start_col = get_out_of_matrix(command,current_row,current_col,size)

if is_won:
    print('Player won!')
else:
    print('Player lost!')

[print(''.join(el)) for el in matrix]

