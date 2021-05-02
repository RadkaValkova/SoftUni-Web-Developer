file_path = '/13_file_handling/files/demo.txt'

file = open(file_path, 'r')

# print(file.read(3))
# print(file.read())
# print(file.readline(5))
# print(file.readline(5))
# print(file.readline(5))
# print(file.readline())

while True:
    line = file.readline()
    if not line:
        break
    print(line)

# while True:
#     line = file.readline(15)
#     if not line:
#         break
#     print(line)

# while True:
#     line = file.read(15)
#     if not line:
#         break
#     print(line)