n = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]
flattened_matrix = [x
                    for row in matrix
                    for x in row]

print(flattened_matrix)



