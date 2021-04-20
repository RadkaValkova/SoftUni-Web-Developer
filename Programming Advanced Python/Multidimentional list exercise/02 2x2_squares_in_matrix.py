def get_square_with_equal_elements(matrix, row, col):
    result = []
    if matrix[row][col] == matrix[row][col+1] == matrix[row+1][col] == matrix[row+1][col+1]:
        result.append(matrix[row][col])
        result.append(matrix[row][col+1])
        result.append(matrix[row+1][col])
        result.append(matrix[row+1][col+1])
    return result


def read_list_from_input(separator=' '):
    return [el for el in input().split()]


(row_count, column_count) = [int(x) for x in input().split()]
matrix = []
for _ in range(row_count):
    matrix.append(read_list_from_input())

result_count = 0
for r in range(row_count-1):
    for c in range(column_count-1):
        result = get_square_with_equal_elements(matrix,r, c)
        if result:
            result_count += 1
print(result_count)

# def read_matrix():
#     row_count, column_count = [int(x) for x in input().split()]
#     matrix = []
#     for _ in range(row_count):
#         row = [el for el in input().split()]
#         matrix.append(row)
#     return matrix
#
#
# def get_sub_matrix(matrix, r, c):
#     size = 2
#     el = matrix[r][c]
#     sub_matrix = []
#     for row_ind in range(r, r+size):
#         row = []
#         for col_ind in range(c, c+size):
#             element = matrix[row_ind][col_ind]
#             if element == el:
#                 row.append(element)
#         sub_matrix.append(row)
#     return sub_matrix
#
#
# matrix = read_matrix()
# counter = 0
#
# for row_index in range(len(matrix)-1):
#     for col_index in range(len(matrix[row_index])-1):
#         current_sub_matrix = get_sub_matrix(matrix,row_index,col_index)
#         result = 0
#         for r_index in current_sub_matrix:
#             result += len(r_index)
#             if result == 4:
#                 counter +=1
#
# print(counter)


