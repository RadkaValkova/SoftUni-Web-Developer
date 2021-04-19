def read_matrix():
    (row_count, col_count) = [int(el) for el in input().split(', ')]
    matrix = []
    for row_ind in range(row_count):
        row = [int(el) for el in input().split(', ')]
        matrix.append(row)
    return matrix


def get_sub_matrix_sum(matrix, row_ind, col_ind):
    size = 2
    result = 0
    for r in range(row_ind, row_ind + size):
        for c in range(col_ind,col_ind + size):
            result += matrix[r][c]
    return result


def print_result(matrix,r,c):
    for i in range(r, r + 2):
        for j in range(c,c+2):
            print(matrix[i][j], end=' ')
        print()


matrix = read_matrix()
max_matrix = get_sub_matrix_sum(matrix, 0, 0)
max_row, max_col = (0,0)

for row in range(len(matrix)-1):
    for col in range(len(matrix[0])-1):
        current_sum = get_sub_matrix_sum(matrix, row, col)
        if current_sum > max_matrix:
            max_matrix = current_sum
            max_row, max_col = row,col

print(max_matrix)
print(max_row, max_col)
print_result(matrix,max_row,max_col)
