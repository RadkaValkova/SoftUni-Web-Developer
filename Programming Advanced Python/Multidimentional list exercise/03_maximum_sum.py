def read_matrix():
    row_count, column_count = [int(x) for x in input().split()]
    matrix = []
    for _ in range(row_count):
        row = [int(el) for el in input().split()]
        matrix.append(row)
    return matrix


def get_sum_sub_matrix(matrix, r, c):
    size = 3
    result = 0
    for row_index in range(r, r + size):
        for col_index in range(c, c+ size):
            current_el = matrix[row_index][col_index]
            result += current_el
    return result


def print_result(matrix,r,c):
    size = 3
    print(f'Sum = {get_sum_sub_matrix(matrix,r,c)}')
    for row in range(r, r+size):
        current_row = []
        for col in range(c, c +size):
            current_row.append(matrix[row][col])
        print(' '.join(str(el) for el in current_row))


matrix = read_matrix()
max_matrix_sum = get_sum_sub_matrix(matrix,0,0)
max_row, max_col = (0,0)

for row_ind in range(len(matrix)-2):
    for col_ind in range(len(matrix[row_ind])-2):
        sum_sub_matrix = get_sum_sub_matrix(matrix,row_ind,col_ind)
        if sum_sub_matrix > max_matrix_sum:
            max_matrix_sum = sum_sub_matrix
            max_row, max_col = row_ind,col_ind

print_result(matrix, max_row, max_col)
