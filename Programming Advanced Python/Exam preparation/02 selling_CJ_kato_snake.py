def read_matrix(n):
    matrix = []
    for _ in range(n):
        row = [el for el in input()]
        matrix.append(row)
    return matrix


def snake_start_position(matrix,n):
    start_row = 0
    start_col = 0
    for r in range(n):
        for c in range(n):
            if matrix[r][c] == 'S':
                start_row = r
                start_col = c
    return start_row, start_col


def get_new_position(command, row,col):
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
    return new_row,new_col


def get_exit_of_the_lair(matrix,n,row,col):
    new_row = 0
    new_col = 0
    for r in range(n):
        for c in range(n):
            if matrix[r][c] == 'O':
                if (r,c) != (row,col):
                    new_row = r
                    new_col = c
                    break
    return new_row,new_col


n = int(input())
matrix = read_matrix(n)

money = 0
start_row = snake_start_position(matrix, n)[0]
start_col = snake_start_position(matrix, n)[1]
is_won = True

while True:
    current_command = input()
    if not current_command:
        break
    new_row,new_col = get_new_position(current_command,start_row,start_col)
    if (0 > new_row or new_row >= n) or (0 > new_col or new_col >= n):
        matrix[start_row][start_col] = '-'
        is_won = False
        print('Bad news, you are out of the bakery.')
        break

    elif matrix[new_row][new_col].isdigit():
        money += int(matrix[new_row][new_col])
        matrix[new_row][new_col] = 'S'
        matrix[start_row][start_col] = '-'
        start_row = new_row
        start_col = new_col
        if money >= 50:
            break

    elif matrix[new_row][new_col] == '-':
        matrix[new_row][new_col] = 'S'
        matrix[start_row][start_col] = '-'
        start_row = new_row
        start_col = new_col

    elif matrix[new_row][new_col] == 'O':
        matrix[start_row][start_col] = '-'
        matrix[new_row][new_col] = '-'
        start_row,start_col = get_exit_of_the_lair(matrix,n,new_row,new_col)
        matrix[start_row][start_col] = 'S'

if is_won:
    print('Good news! You succeeded in collecting enough money!')
print(f'Money: {money}')
[print(''.join(el)) for el in matrix]



