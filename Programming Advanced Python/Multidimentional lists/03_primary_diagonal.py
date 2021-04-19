def read_matrix():
    rows_count = int(input())
    matrix = []
    for _ in range(rows_count):
        row = [int(el) for el in input().split()]
        matrix.append(row)
    return matrix


def get_sum_primary_diagonal(matrix):
    sum_diagonal = 0
    for row_index in range(len(matrix)):
        for column_index in range(len(matrix)):
            if row_index == column_index:
                sum_diagonal += matrix[row_index][column_index]
    return sum_diagonal


def get_sum_secondary_diagonal(matrix):
    sum_diagonal = 0
    for row_index in range(len(matrix)):
        for column_index in range(len(matrix)):
            column_index = len(matrix) - row_index - 1
            current_el = matrix[row_index][column_index]
            sum_diagonal += current_el
            break
    return sum_diagonal


def get_sum_below_primary(matrix):
    sum_below = 0
    for row_index in range(len(matrix)):
        for column_index in range(len(matrix)):
            current_el = matrix[row_index][column_index]
            sum_below += current_el
            if column_index <= row_index: # including diagonal
            # if column_index < row_index: exluding diagonal
                sum_below += current_el
    return sum_below


def get_sum_above_primary(matrix):
    sum_above = 0
    size = len(matrix)
    for row_index in range(size):
        for column_index in range(row_index,size):
            current_el = matrix[row_index][column_index]
            sum_above += current_el
    return sum_above


matrix = read_matrix()
result = get_sum_primary_diagonal(matrix)
result1 = get_sum_secondary_diagonal(matrix)
print(result)
print(result1)
print(get_sum_below_primary(matrix))
print(get_sum_above_primary(matrix))