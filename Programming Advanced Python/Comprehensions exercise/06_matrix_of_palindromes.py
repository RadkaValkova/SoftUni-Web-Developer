(rows_count, col_count) = map(int, input().split())

matrix = []

for i in range(ord('a'), ord('a') + rows_count):
    row = []
    for j in range(i, i + col_count):
        row.append(f'{chr(i)}{chr(j)}{chr(i)}')

    matrix.append(row)

[print(' '.join(el)) for el in matrix]