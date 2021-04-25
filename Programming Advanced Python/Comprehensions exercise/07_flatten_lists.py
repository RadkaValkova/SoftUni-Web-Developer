matrix = [[int(el) for el in x.split()] for x in input().split('|')]
flattened_matrix = ' '.join([str(num) for row in matrix[::-1] for num in row])

print(flattened_matrix)