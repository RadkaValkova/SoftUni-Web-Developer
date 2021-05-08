def is_valid_position(row,col,size):
    return 0<=row<size and 0<=col<size


text = list(input())
size = int(input())
matrix = [(list(input())) for _ in range(size)]
start_pos = [(x,y) for x in range(size) for y in range(size) if matrix[x][y] == 'P']
command_move = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
start_row = start_pos[0][0]
start_col = start_pos[0][1]

while True:
    command = input()
    if command == 'end':
        break
    if command in command_move:
        new_row = start_row + command_move[command][0]
        new_col = start_col + command_move[command][1]
        if is_valid_position(new_row,new_col,size):
            matrix[start_row][start_col] = '-'
            if matrix[new_row][new_col] != '-' and matrix[new_row][new_col] != 'P':
                text.append(matrix[new_row][new_col])
                matrix[new_row][new_col] = 'P'
            start_row,start_col = new_row,new_col
        else:
            if text:
                text.pop()

print(''.join(text))
[print(''.join(row)) for row in matrix]

