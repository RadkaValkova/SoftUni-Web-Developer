# file_path = 'C:/Users/User/Desktop/Plovdiv.txt'
#
# file = open(file_path, 'r')
# print(file.read())

file_path = '/13_file_handling/files/demo.txt'

file = open(file_path, 'r')
# lines = file.readlines()
# print(lines)
#
# for line in lines:
#     print(line)

index = 1
for line in file:
    print(f'{index}. {line.strip()}')
    index += 1
