def is_valid_position(row, col, size):
    return 0 <= row < size and 0 <= col < size


def count_nice_kids(matrix,size):
    result = 0
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'V':
                result += 1
    return result


def give_cookies_presents(matrix,row,col,move,kids,presents):
    for value in move.values():
        if matrix[row + value[0]][col + value[1]] == 'X':
            presents-= 1
        elif matrix[row + value[0]][col + value[1]] == 'V':
            presents -= 1
            kids -= 1
        matrix[row + value[0]][col + value[1]] = '-'
    return matrix,presents,kids


presents_number = int(input())
matrix_size = int(input())
matrix = [list(input().split()) for _ in range(matrix_size)]
move_dict = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
start_position = [(x, y) for x in range(0, matrix_size) for y in range(0, matrix_size) if matrix[x][y] == "S"]
nice_kids_begining = count_nice_kids(matrix, matrix_size)
nice_kids = nice_kids_begining

start_row = start_position[0][0]
start_col = start_position[0][1]

while presents_number > 0:
    command = input()
    if command == 'Christmas morning':
        break
    new_row = start_row + move_dict[command][0]
    new_col = start_col + move_dict[command][1]
    matrix[start_row][start_col] = '-'
    if is_valid_position(new_row, new_col, matrix_size):
        if matrix[new_row][new_col] == 'X':
            pass
            # matrix[new_row][new_col] = 'S'
        elif matrix[new_row][new_col] == 'V':
            presents_number -= 1
            nice_kids_begining -= 1
            matrix[new_row][new_col] = 'S'
        elif matrix[new_row][new_col] == 'C':
            matrix,presents_number,nice_kids_begining = give_cookies_presents(matrix,new_row,new_col,move_dict,
                                                                              presents_number,nice_kids_begining)
            matrix[new_row][new_col] = 'S'
        elif matrix[new_row][new_col] == '-':
            matrix[new_row][new_col] = 'S'
    else:
        print('Santa ran out of presents.')
        break
    start_row = new_row
    start_col = new_col


[print(' '.join(el)) for el in matrix]
if nice_kids_begining <= 0:
    print(f'Good job, Santa! {nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids_begining} nice kid/s.')

