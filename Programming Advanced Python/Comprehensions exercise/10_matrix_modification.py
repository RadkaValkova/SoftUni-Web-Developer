def valid_indexes(row,col, size):
    return 0 <= row < size and 0 <= col <= size


n = int(input())

matrix = [[int(el) for el in input().split()] for x in range(n)]

while True:
    line = input()
    if line == 'END':
        break
    (command, row, col, value) = line.split()
    row = int(row)
    col = int(col)
    value = int(value)
    if command == 'Add':
        if valid_indexes(row,col,n):
            matrix[row][col] += value
        else:
            print('Invalid coordinates')
    elif command == 'Subtract':
        if valid_indexes(row,col,n):
            matrix[row][col] -= value
        else:
            print('Invalid coordinates')

[print(' '.join([str(el) for el in row])) for row in matrix]
