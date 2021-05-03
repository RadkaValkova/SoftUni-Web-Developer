import os


def sort_files(files_list):
    files_library = {}
    for file in files_list:
        file_name, extension = file.split(".")
        if extension not in files_library:
            files_library[extension] = []
        files_library[extension].append(file_name)

    sorted_files = sorted(files_library.items(), key=lambda x: x[0])
    return sorted_files


result = ''
dir_content = os.listdir('C:\Users\User\PycharmProjects\Advanced\14_file_handling_exercise\04 directory_traversalExample')
files = [file for file in dir_content if "." in file]

for extension, file_names in sort_files(files):
    result += f'.{extension}\n'
    for name in file_names:
        result += f"- - - {name}.{extension}\n"

with open('C:\\Users\\SMan\\Desktop\\report.txt', 'w') as file:
    file.writelines(result)