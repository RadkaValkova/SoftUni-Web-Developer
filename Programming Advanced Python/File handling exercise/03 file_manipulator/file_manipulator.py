import os

while True:
    line = input()
    if line == 'End':
        break
    tokens = line.split('-')
    command = tokens[0]
    file_name = tokens[1]
    if command == 'Create':
        with open(file_name, 'w') as file:
            file.write('')

    elif command == 'Add':
        content = tokens[2]
        with open(file_name, 'a') as file_name:
            file_name.write(content)
            file_name.write('\n')

    elif command == 'Replace':
        old_string, new_string = tokens[2], tokens[3]
        if os.path.exists(file_name):
            text = ''
            with open(file_name, 'r') as file:
                text = file.read()
            text = text.replace(old_string,new_string)
            with open(file_name, 'w') as file:
                file.write(text)
        else:
            print('An error occurred')

    elif command == 'Delete':
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print('An error occurred')