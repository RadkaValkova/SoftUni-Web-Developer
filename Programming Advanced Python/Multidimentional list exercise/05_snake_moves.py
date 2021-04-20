from collections import deque

(rows_count, columns_count) = [int(x) for x in input().split()]
snake = deque([x for x in input()])
matrix = []

# for r in range(rows_count):
#     row = []
#     for c in range(columns_count):
#         current = snake.popleft()
#         row.append(current)
#         snake.append(current)
#     if r % 2 == 0:
#         matrix.append(row)
#     else:
#         matrix.append(row[::-1])
#
# for r in range(rows_count):
#     for c in range(columns_count):
#         print(matrix[r][c], end='')
#     print()

for r in range(rows_count):
    matrix.append([])
    for c in range(columns_count):
        matrix[r].append('')

for row in range(rows_count):
    for col in range(columns_count):
        current_col = col
        current_char = snake.popleft()
        if row % 2 != 0:
            current_col = columns_count - current_col - 1
        matrix[row][current_col] = current_char
        snake.append(current_char)

for row in matrix:
    print(''.join(row))