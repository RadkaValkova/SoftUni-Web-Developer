def is_valid_index(s, r, c):
    return 0 <= r < s and 0 <= c < size


def get_bombs_number(matrix, r, c, move):
    result = 0
    for i in range(len(move)):
        row = r + move[i][0]
        col = c + move[i][1]
        if is_valid_index(len(matrix),row,col):
            if matrix[row][col] == '*':
                result += 1
    return result


size = int(input())
bombs_number = int(input())
matrix = [[0] * size for _ in range(size)]
move = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

for _ in range(bombs_number):
    position = [int(el) for el in input() if el.isdigit()]
    row = position[0]
    col = position[1]
    matrix[row][col] = '*'

for r in range(size):
    for c in range(size):
        if matrix[r][c] == 0:
            matrix[r][c] = get_bombs_number(matrix, r, c, move)

[print(' '.join([str(x) for x in el])) for el in matrix]


# def read_matrix(n):
#     matrix = []
#     for _ in range(n):
#         row = [0] * n
#         matrix.append(row)
#     return matrix
#
#
# def read_bombs_indexes(number):
#     indexes = []
#     for _ in range(number):
#         current = [el for el in input() if el.isdigit()]
#         indexes.append(current)
#     return indexes
#
#
# def put_bombs(matrix, b_ind):
#     for i in range(len(b_ind)):
#         current_row = int(b_ind[i][0])
#         current_col = int(b_ind[i][1])
#         matrix[current_row][current_col] = '*'
#     return matrix
#
#
# def is_valid_index(n, r, c):
#     return 0 <= r < n and 0 <= c < n
#
#
# def calculate_position(matrix, r, c):
#     next_cells = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]
#     result = 0
#     for i in range(len(next_cells)):
#         current_r = r + next_cells[i][0]
#         current_c = c + next_cells[i][1]
#         if is_valid_index(len(matrix),current_r,current_c):
#             if matrix[current_r][current_c] == '*':
#                 result += 1
#     return result
#
#
# n = int(input())
# bombs_number = int(input())
# bombs_indexes = read_bombs_indexes(bombs_number)
# matrix = read_matrix(n)
# matrix = put_bombs(matrix, bombs_indexes)
#
# for row in range(n):
#     for col in range(n):
#         if matrix[row][col] != '*':
#             matrix[row][col] = calculate_position(matrix, row, col)
#
# [print(" ".join(str(x) for x in el)) for el in matrix]

