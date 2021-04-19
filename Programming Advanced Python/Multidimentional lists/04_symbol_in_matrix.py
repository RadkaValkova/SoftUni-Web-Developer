def read_matrix():
    size = int(input())
    matrix = []
    for _ in range(size):
        row = [el for el in input()]
        matrix.append(row)
    return matrix


def find_symbol(matrix,symbol):
    for row_ind in range(len(matrix)):
        for col_ind in range(len(matrix[row_ind])):
            current_symbol = matrix[row_ind][col_ind]
            if current_symbol == symbol:
                return f'({row_ind}, {col_ind})'


def print_result(result,symbol):
    if result:
        print(result)
    else:
        print(f'{symbol} does not occur in the matrix')


matrix = read_matrix()
symbol = input()
print_result(find_symbol(matrix,symbol),symbol)


