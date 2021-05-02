file_path = '/13_file_handling/files/to_write.txt'
# 'w' mode creates a new file if it doesn't exist or if it exists !!!!clear the existing information in it'
# file = open(file_path, 'w')
#
# file.write('Pesho')
# file.write('Gosho')

# print('Pesho', file=file) do the same as file.write but on new lines
# print('Gosho', file=file)

# 'a' mode append info at the end of the existing file
file = open(file_path, 'a')
# file.write('   mama mia')

# 'x' mode creates a new file if it doesn't exist and if it exists give an exeption error'

file.writelines('  EEEEE\n') # every time executing it, add the strin in the file, without writing new commands to
file.close()

with open(file_path, 'a') as file2: # вместо да затваряме файла
    file2.writelines(['Stamat\n', 'Mimi\n'])
