(rows_count, columns_count) = (int(x) for x in input().split(', '))

matrix = []

for _ in range(rows_count):
    row = [int(el) for el in input().split(' ')]
    matrix.append(row)

column_sum = [0] * columns_count

for row in range(rows_count):
    for column in range(columns_count):
        column_sum[column] += matrix[row][column]

[print(col_sum) for col_sum in column_sum]



