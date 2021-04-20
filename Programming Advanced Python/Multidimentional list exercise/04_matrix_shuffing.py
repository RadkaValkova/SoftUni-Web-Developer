def read_list_from_input(separator= ' '):
    return [el for el in input().split()]


def swap_elements(matrix, row1, col1, row2, col2):
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    return matrix


def print_matrix(matrix, row, col):
    for r in range(row):
        for c in range(col):
            print(matrix[r][c], end=" ")
        print()


(rows_count, columns_count) = (int(x) for x in input().split())
matrix = [read_list_from_input() for _ in range(rows_count)]

while True:
    line = input()
    if line == 'END':
        break
    line = line.split()
    if len(line) != 5 or line[0] != 'swap':
        print('Invalid input!')
    else:
        (command, row1, col1, row2, col2) = line
        row1 = int(row1)
        col1 = int(col1)
        row2 = int(row2)
        col2 = int(col2)
        if (row1 or row2) in range(rows_count) or (col1 or col2) in range(columns_count):
            print_matrix(swap_elements(matrix, row1, col1, row2, col2), rows_count, columns_count)
        else:
            print('Invalid input!')


# def read_matrix():
#     row_count, column_count = [int(x) for x in input().split()]
#     matrix = []
#     for _ in range(row_count):
#         row = [el for el in input().split()]
#         matrix.append(row)
#     return matrix
#
#
# def get_swap_of_elements(matrix,r1,c1,r2,c2):
#     matrix[r1][c1],matrix[r2][c2] = matrix[r2][c2],matrix[r1][c1]
#
#
# def command_is_valid(matrix,r1,c1,r2,c2):
#     if 0 <= r1 < len(matrix) and 0 <= c1 < len(matrix[0]) and 0 <= r2 < len(matrix) and 0 <= c2 < len(matrix[0]):
#         return True
#     return False
#
#
# matrix = read_matrix()
#
# while True:
#     line = input()
#     if line == 'END':
#         break
#     tokens = line.split()
#     command = tokens[0]
#     if command != 'swap' and len(tokens) != 5:
#         print('Invalid input!')
#     else:
#         tokens_list = []
#         for el in tokens:
#             if el.isdigit():
#                 tokens_list.append(int(el))
#         row1, col1, row2, col2 = tokens_list
#         if command_is_valid(matrix,row1, col1, row2, col2):
#             get_swap_of_elements(matrix, row1, col1, row2, col2)
#             [print(' '.join([el for el in row])) for row in matrix]
#         else:
#             print('Invalid input!')


