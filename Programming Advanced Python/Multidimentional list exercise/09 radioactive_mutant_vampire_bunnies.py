def read_matrix_and_start(n):
    matrix = []
    start_pos = (0, 0)
    for i in range(n):
        row = [el for el in input()]
        matrix.append(row)
        if 'P' in row:
            start_pos = (i, row.index('P'))
    return matrix, start_pos


def get_player_move(command, r, c):
    new_row = r
    new_col = c
    if command == 'R':
        new_col = c + 1
    elif command == 'L':
        new_col = c - 1
    elif command == 'U':
        new_row = r - 1
    elif command == 'D':
        new_row = r + 1
    return new_row, new_col


def get_bunnies_positions(matrix):
    b_positions = []
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'B':
                b_positions.append((r, c))
    return b_positions


def spread_bunnies(matrix, pos):
    for p in range(len(pos)):
        current_b_row = pos[p][0]
        current_b_col = pos[p][1]
        for i in range(len(pos)):
            if current_b_col - 1 in range(len(matrix[0])):
                matrix[current_b_row][current_b_col - 1] = 'B'
            if current_b_row - 1 in range(len(matrix)):
                matrix[current_b_row - 1][current_b_col] = 'B'
            if current_b_col + 1 in range(len(matrix[0])):
                matrix[current_b_row][current_b_col + 1] = 'B'
            if current_b_row + 1 in range(len(matrix)):
                matrix[current_b_row + 1][current_b_col] = 'B'
    return matrix


row_count, col_count = [int(el) for el in input().split()]
matrix, start_position = read_matrix_and_start(row_count)
commands = [el for el in input()]
start_row = start_position[0]
start_col = start_position[1]

is_winner = False
loos_result = ''

for i in range(len(commands)):
    current_command = commands[i]
    new_position = get_player_move(current_command, start_row, start_col)
    matrix[start_col][start_col] = '.'
    new_row = new_position[0]
    new_col = new_position[1]
    if (0 > new_row or new_col >= row_count) or (0 > new_col or new_col >= col_count):
        is_winner = True
        b_positions = get_bunnies_positions(matrix)
        matrix = spread_bunnies(matrix, b_positions)
        break
    elif 0 <= new_row < row_count and 0 <= new_col < col_count:
        if matrix[new_row][new_col] == 'B':
            is_winner = False
            loos_result = f'dead: {new_row} {new_col}'
            b_positions = get_bunnies_positions(matrix)
            matrix = spread_bunnies(matrix, b_positions)
            break
        else:
            b_positions = get_bunnies_positions(matrix)
            matrix = spread_bunnies(matrix, b_positions)

    start_row = new_row
    start_col = new_col

[print(''.join(row)) for row in matrix]
if is_winner:
    print(f'won: {start_row} {start_col}')
else:
    print(loos_result)
