path = input().split('\\')

tokens = path[-1].split('.')
file_name = tokens[0]
file_extension = tokens[1]

print(f'File name: {file_name}')
print(f'File extension: {file_extension}')