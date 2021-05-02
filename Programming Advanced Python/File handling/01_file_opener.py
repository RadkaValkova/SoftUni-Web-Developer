file_path = '/13_file_handling/files/File Opener/text.txt'

try:
    open(file_path, 'r')
    print('File found')
except:
    print('File not found')