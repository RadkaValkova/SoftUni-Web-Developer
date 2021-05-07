def is_valid_position(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = int(input())
matrix = [(list(input())) for _ in range(size)]
command_move = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

find_bee_pos = [(x, y) for x in range(size) for y in range(size) if matrix[x][y] == 'B']
start_row = find_bee_pos[0][0]
start_col = find_bee_pos[0][1]
flowers = 0
is_won = True

while True:
    command = input()
    if command == 'End':
        break
    if command in command_move:
        new_row = start_row + command_move[command][0]
        new_col = start_col + command_move[command][1]
        if is_valid_position(new_row, new_col, size):
            matrix[start_row][start_col] = '.'
            if matrix[new_row][new_col] == 'f':
                flowers += 1
                matrix[new_row][new_col] = 'B'
            elif matrix[new_row][new_col] == 'O':
                matrix[new_row][new_col] = '.'
                new_row = new_row + command_move[command][0]
                new_col = new_col + command_move[command][1]
                if matrix[new_row][new_col] == 'f':
                    flowers += 1
                matrix[new_row][new_col] = 'B'
            elif matrix[new_row][new_col] == '.':
                matrix[new_row][new_col] = 'B'
        else:
            matrix[start_row][start_col] = '.'
            print('The bee got lost!')
            break
        start_row, start_col = new_row, new_col

if flowers < 5:
    print(f'The bee couldn\'t pollinate the flowers, she needed {5 - flowers} flowers more')
else:
    print(f'Great job, the bee managed to pollinate {flowers} flowers!')

[print(''.join(el)) for el in matrix]
