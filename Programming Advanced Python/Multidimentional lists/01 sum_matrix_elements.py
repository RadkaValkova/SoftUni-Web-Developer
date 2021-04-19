(rows, columns) = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(',')]
    matrix.append(row)

sum_matrix = sum([sum(el) for el in matrix])
print(sum_matrix)
print(matrix)