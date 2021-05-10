def is_valid_index(size,row,col):
    return 0<=row<size and 0<=col<size

size = int(input())
matrix = [[el for el in input().split()] for _ in range(size)]
bunny_position = [(x,y) for x in range(size) for y in range(size) if matrix[x][y] == 'B']
movement_dict = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
key = ''
index_eggs = []
up_sum = {'up': 0, 'indexes': []}
down_sum = {'down': 0, 'indexes': []}
left_sum = {'left': 0, 'indexes': []}
right_sum = {'right': 0, 'indexes': []}

bunny_row,bunny_col = bunny_position[0][0], bunny_position[0][1]

for r in range(size):
    for c in range(size):
        if key == 'up':
            current_row = bunny_row + movement_dict[key][0]
            current_col = bunny_col + movement_dict[key][1]
            if is_valid_index(size,current_row,current_col) and matrix != 'X':
                up_sum['up'] += int(matrix[current_row][current_col])
                up_sum['indexes'].append([current_row,current_col])
            else:
                break
            bunny_row, bunny_col = current_row, current_col

for r in range(size):
    for c in range(size):
        if key == 'down':
            current_row = bunny_row + movement_dict[key][0]
            current_col = bunny_col + movement_dict[key][1]
            if is_valid_index(size,current_row,current_col) and matrix != 'X':
                up_sum['down'] += int(matrix[current_row][current_col])
                up_sum['indexes'].append([current_row,current_col])
            else:
                break
            bunny_row, bunny_col = current_row, current_col

for r in range(size):
    for c in range(size):
        if key == 'left':
            current_row = bunny_row + movement_dict[key][0]
            current_col = bunny_col + movement_dict[key][1]
            if is_valid_index(size,current_row,current_col) and matrix != 'X':
                up_sum['left'] += int(matrix[current_row][current_col])
                up_sum['indexes'].append([current_row,current_col])
            else:
                break
            bunny_row, bunny_col = current_row, current_col

for r in range(size):
    for c in range(size):
        if key == 'right':
            current_row = bunny_row + movement_dict[key][0]
            current_col = bunny_col + movement_dict[key][1]
            if is_valid_index(size,current_row,current_col) and matrix != 'X':
                up_sum['right'] += int(matrix[current_row][current_col])
                up_sum['indexes'].append([current_row,current_col])
            else:
                break
            bunny_row, bunny_col = current_row, current_col


print(up_sum)
print(down_sum)
print(left_sum)
print(right_sum)