def read_matrix():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix


def sum_primary_diagonal(matrix):
    result = 0
    for i in range(len(matrix)):
        result += matrix[i][i]
    return result


def sum_secondary_diagonal(matrix):
    size = len(matrix)
    result = 0
    for r in range(size):
        for c in range(size):
            result += matrix[r][size-r-1]
            break
    return result


matrix = read_matrix()
print(sum_primary_diagonal(matrix))
print(sum_secondary_diagonal(matrix))
print(abs(sum_primary_diagonal(matrix) - sum_secondary_diagonal(matrix)))
