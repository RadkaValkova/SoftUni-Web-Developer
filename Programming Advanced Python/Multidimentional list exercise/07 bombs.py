def read_matrix(n):
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split(' ')]
        matrix.append(row)
    return matrix


def get_exploded_cells_value(matrix, row, col):
    cells_pos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(len(cells_pos)):
        current_ind = cells_pos[i]
        cell_row = row + current_ind[0]
        cell_col = col + current_ind[1]
        temp = int(matrix[row][col])
        if cell_row in range(len(matrix)) and cell_col in range(len(matrix)):
            if matrix[cell_row][cell_col] <= 0:
                continue
            else:
                matrix[cell_row][cell_col] -= temp
    matrix[row][col] = 0
    return matrix


size = int(input())
matrix = read_matrix(size)
bombs_ind = [el for el in input().split(' ')]

sum_elements = 0
cells_counter = 0

for i in range(len(bombs_ind)):
    indexes = bombs_ind[i].split(',')
    current_row_ind = int(indexes[0])
    current_col_ind = int(indexes[1])
    current_bomb = matrix[current_row_ind][current_col_ind]
    matrix = get_exploded_cells_value(matrix, current_row_ind, current_col_ind)

for element in matrix:
    current_sum = sum(el for el in element if el > 0)
    sum_elements += current_sum
    current_count = len([el for el in element if el > 0])
    cells_counter += current_count

print(f'Alive cells: {cells_counter}')
print(f'Sum: {sum_elements}')
for row in matrix:
    print(' '.join(str(el) for el in row))


