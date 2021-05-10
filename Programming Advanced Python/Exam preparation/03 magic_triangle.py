# def get_magic_triangle(n):
#     matrix = []
#     for i in range(1, n+1):
#         row = [1] * i
#         matrix.append(row)
#     for r in range(2,n):
#         for c in range(1, r):
#             matrix[r][c] = matrix[r-1][c-1] + matrix[r-1][c]
#     print(matrix)
#
#
# get_magic_triangle(5)

# def get_magic_triangle(num):
#     result = []
#     x = [1]
#     y = [0]
#     for _ in range(num):
#         result.append(x)
#         x = [i+j for i, j in zip(x+y, y+x)]
#     return result
#
#
# print(get_magic_triangle(5))

def printPascal(n):
    for line in range(1,n + 1):
        C = 1 # used to represent C(line, i)
        for i in range(1, line + 1):
            # The first value in a
            # line is always 1
            print(C, end = " ")
            C = int(C * (line - i) / i)
        print("")
n = 5
printPascal(n)
