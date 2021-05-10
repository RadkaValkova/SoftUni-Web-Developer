def is_valid_position(size,row,col):
    return 0<=row<size and 0<=col<size


def get_current_position(direction, step, row, col):
    current_row, current_col = row,col
    if direction == 'right':
        current_row, current_col = row,col+step
    elif direction == 'left':
        current_row, current_col = row,col-step
    elif direction == 'up':
        current_row, current_col = row-step,col
    elif direction == 'down':
        current_row, current_col = row+step,col
    return current_row,current_col


size = int(input())
matrix = [[el for el in input().split()] for _ in range(size)]
plane_position = [(x,y) for x in range(size) for y in range(size) if matrix[x][y] == 'p']
target_number = len([x for x in range(size) for y in range(size) if matrix[x][y] == 't'])

start_row = plane_position[0][0]
start_col = plane_position[0][1]
shooted_targets = 0

for i in range(int(input())):
    line = input().split()
    command = line[0]
    direction = line[1]
    step = int(line[2])
    if command == 'move':
        current_pos = get_current_position(direction,step,start_row,start_col)
        current_row, current_col = current_pos[0],current_pos[1]
        if is_valid_position(size,current_row,current_col) and matrix[current_row][current_col] == '.':
            matrix[current_row][current_col] = 'p'
            matrix[start_row][start_col] = '.'
            start_row,start_col = current_row,current_col
    elif command == 'shoot':
        current_pos = get_current_position(direction, step, start_row, start_col)
        current_row, current_col = current_pos[0], current_pos[1]
        if is_valid_position(size, current_row, current_col):
            if matrix[current_row][current_col] == '.':
                matrix[current_row][current_col] = 'x'
            elif matrix[current_row][current_col] == 't':
                shooted_targets +=1
                matrix[current_row][current_col] = 'x'

if target_number == shooted_targets:
    print(f'Mission accomplished! All {target_number} targets destroyed.')
else:
    print(f'Mission failed! {target_number-shooted_targets} targets left.')

[print(' '.join(el)) for el in matrix]

