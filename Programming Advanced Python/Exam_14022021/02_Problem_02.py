import math

def is_valid_positin(size, r, c):
    return 0 <= r < size and 0 <= c < size


size = int(input())
matrix = [[el for el in input().split()] for _ in range(size)]
move_pos = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
player_pos = [(x, y) for x in range(size) for y in range(size) if matrix[x][y] == 'P']

coins = 0
paths = []

start_row = player_pos[0][0]
start_col = player_pos[0][1]

while True:
    command = input()
    if command in move_pos:
        new_row = start_row + move_pos[command][0]
        new_col = start_col + move_pos[command][1]
        if is_valid_positin(size,new_row,new_col) and matrix[new_row][new_col] != 'X':
            coins += int(matrix[new_row][new_col])
            paths.append([new_row,new_col])
            start_row,start_col = new_row,new_col
            if coins >= 100:
                print(f'You won! You\'ve collected {coins} coins.')
                break
        else:
            coins = coins /2
            print(f'Game over! You\'ve collected {math.floor(coins)} coins.')
            break


print('Your path:')
[print(el) for el in paths]
