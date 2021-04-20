def is_valid(position, size):
    row = position[0]
    col = position[1]
    return 0 <= row < size and 0 <= col < size


def get_killed_knights(row, col, size, matrix):
    killed_knights = 0
    rows = [-2, -1, 1, 2, 2, 1, -1, -2]
    columns = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(len(rows)):
        current_position = [row + rows[i], col + columns[i]]
        if is_valid(current_position, size) and matrix[current_position[0]][current_position[1]] == 'K':
            killed_knights += 1
    return killed_knights


n = int(input())
matrix = []
killed_knights_counter = 0

for _ in range(n):
    line = [x for x in input()]
    matrix.append(line)

while True:
    most_kills = 0
    to_kill = []

    for row in range(n):
        for col in range(n):
            if matrix[row][col] == 'K':
                killed_knights = get_killed_knights(row, col, n, matrix)
                if killed_knights > most_kills:
                    most_kills = killed_knights
                    to_kill = [row, col]

    if most_kills == 0:
        break

    to_kill_row = to_kill[0]
    to_kill_col = to_kill[1]
    matrix[to_kill_row][to_kill_col] = '0'
    killed_knights_counter += 1

print(killed_knights_counter)
