SIZE = 8


def is_valid_position(size,row,col):
    return 0<= row < size and 0 <= col < size


def get_capture_queens(matrix,size,k_row, k_col,move_dict,key):
    positions = []
    start_row = k_row
    start_col = k_col
    while True:
        current_row = start_row + move_dict[key][0]
        current_col = start_col + move_dict[key][1]
        if not is_valid_position(size,current_row,current_col):
            break
        else:
            if matrix[current_row][current_col] == 'Q':
                positions.append([current_row,current_col])
                break
        start_row,start_col = current_row,current_col
    return positions


matrix = [[el for el in input().split()] for _ in range(SIZE)]
king_positions = [(x,y) for x in range(SIZE) for y in range(SIZE) if matrix[x][y] == 'K']
move_dict = {'l_up':(-1,-1), 'up': (-1,0), 'r_up': (-1,1), 'right': (0,1), 'r_down': (1,1), 'down': (1,0), 'l_down':(1,-1), 'left':(0,-1)}

king_row = king_positions[0][0]
king_col = king_positions[0][1]
captured_queens = []

for key in move_dict.keys():
    result = get_capture_queens(matrix,SIZE,king_row,king_col,move_dict,key)
    if result:
        captured_queens.append(result)

if captured_queens:
    [print(*el) for el in captured_queens]
else:
    print('The king is safe!')

# QUEEN = 'Q'
# KING = 'K'
# SIZE = 8
# SAFE_KING_MSG = 'The king is safe!'
#
#
# def plus(a, b): return a + b
#
#
# def minus(a, b): return a - b
#
#
# DIRECTIONS = [
#     (None, plus),  # right
#     (None, minus),  # left
#     (plus, None),  # up
#     (minus, None),  # down
#     (plus, plus),  # down right
#     (minus, plus),  # up right
#     (plus, minus),  # down left
#     (minus, minus),  # up left
# ]
#
#
# def get_input():
#     return [input().split(' ') for _ in range(SIZE)]
#
#
# def locate_king(mat):
#     for row_i in range(SIZE):
#         for col_i in range(SIZE):
#             if mat[row_i][col_i] == KING:
#                 return row_i, col_i
#
#
# def is_valid(m, r, c):
#     return 0 <= r < SIZE and 0 <= c < SIZE and m[r][c] == QUEEN
#
#
# def search_direction(mat, x, y, x_operator=None, y_operator=None):
#     for i in range(1, SIZE):
#         row = x_operator(x, i) if x_operator else x
#         col = y_operator(y, i) if y_operator else y
#         if is_valid(mat, row, col):
#             return [row, col]
#
#
# def search_for_queens(mat, x, y):
#     results = [search_direction(mat, x, y, x_op, y_op) for (x_op, y_op) in DIRECTIONS]
#     return list(filter(lambda q: q, results))
#
#
# def print_queens(queens):
#     if queens:
#         [print(queen) for queen in queens]
#     else:
#         print(SAFE_KING_MSG)
#
#
# matrix = get_input()
# king_x, king_y = locate_king(matrix)
# killer_queens = search_for_queens(matrix, king_x, king_y)
# print_queens(killer_queens)