def is_valid_coordinates(row, col, size):
    return 0 <= row < size and 0 <= col < size


def bloom_bloom_plow(matrix, row, col, size):
    for r in range(size):
        if (r, col) != (row, col):
            matrix[r][col] += 1
    for c in range(size):
        if (row, c) != (row, col):
            matrix[row][c] += 1
    return matrix


size_n, m = [int(el) for el in input().split()]
matrix = [[0] * size_n for _ in range(size_n)]
flowers_coordinates = []

while True:
    line = input()
    if line == 'Bloom Bloom Plow':
        for i in range(len(flowers_coordinates)):
            current_row = flowers_coordinates[i][0]
            current_col = flowers_coordinates[i][1]
            if is_valid_coordinates(current_row, current_col, size_n):
                matrix[current_row][current_col] = 1
                matrix = bloom_bloom_plow(matrix, current_row, current_col, size_n)
            else:
                print('Invalid coordinates.')
        break
    else:
        flowers_coordinates.append([int(el) for el in line.split()])

[print(' '.join(str(x) for x in el)) for el in matrix]
