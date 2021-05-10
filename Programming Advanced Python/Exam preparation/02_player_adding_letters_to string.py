def is_valid_position(size, r, c):
    return 0 <= r <= size and 0 <= c < size


string = input()
size = int(input())
matrix = [[x for x in input()] for _ in range(size)]
command_number = int(input())

command_move = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
player_position = [(x, y) for x in range(size) for y in range(size) if matrix[x][y] == 'P']

start_row = player_position[0][0]
start_col = player_position[0][1]

for i in range(command_number):
    current_command = input()
    new_row = start_row + command_move[current_command][0]
    new_col = start_col + command_move[current_command][1]
    if is_valid_position(size, new_row, new_col):
        matrix[start_row][start_col] = '-'
        if matrix[new_row][new_col] != '-':
            string += matrix[new_row][new_col]
        matrix[new_row][new_col] = 'P'
        start_row,start_col = new_row, new_col
    else:
        if string:
            string = string[:-1]

print(string)
[print(el) for el in matrix]
