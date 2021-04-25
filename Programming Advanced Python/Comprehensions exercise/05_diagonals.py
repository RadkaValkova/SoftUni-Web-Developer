n = int(input())
matrix = [[x for x in input().split(', ')] for _ in range(n)]

print(f'First diagonal: {", ".join([matrix[i][i] for i in range(len(matrix))])}. Sum: {sum(int(matrix[i][i]) for i in range(len(matrix)))}')
print(f'Second diagonal: {", ".join([matrix[i][-i-1] for i in range(len(matrix))])}. Sum: {sum(int(matrix[i][-i-1]) for i in range(len(matrix)))}')

