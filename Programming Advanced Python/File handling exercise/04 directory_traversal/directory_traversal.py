import os
files_dict = {}
path = input()
for root, dirs, files in os.walk(path):
    if root.count('\\') > 1:
        continue
    for file in files:
        file_extension = file.split('.')[1]
        if file_extension not in files_dict:
            files_dict[file_extension] = []
        files_dict[file_extension].append(file)

result_str = ''
for key, value in sorted(files_dict.items()):
    result_str += f'.{key}\n'
    for file in sorted(value):
        result_str += f'- - - {file}\n'


desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
final_location = desktop + os.path.sep + 'report.txt'

with open(final_location, 'w') as file:
    file.write(result_str)