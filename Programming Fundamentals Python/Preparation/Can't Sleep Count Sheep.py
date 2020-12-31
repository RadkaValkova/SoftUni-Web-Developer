# sheep_number = int(input())
#
# for i in range(1, sheep_number+1):
#     current_sheep = i
#     print(f'{i} sheep...', end='')

sheep_number = int(input())
message = ''
for i in range(1, sheep_number+1):
    message += f'{i} sheep...'

print(message)