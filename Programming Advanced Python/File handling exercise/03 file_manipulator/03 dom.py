import os


def create_file(f_name):
    with open(f_name, 'w') as file:
        file.write("")


def add_content(f_name, text):
    with open(f_name, 'a') as file:
        file.write(f"{text}\n")


def replace_str_in_file(f_name, str_1, str_2):
    try:
        with open(f_name, 'r+') as file:
            file_text = "".join(file.readlines())
            if str_1 in file_text:
                file_text = file_text.replace(str_1, str_2)
                file.seek(0)
                file.write(file_text)
    except FileNotFoundError:
        print("An error occurred")


def delete_file(f_name):
    try:
        os.remove(f_name)
    except FileNotFoundError:
        print("An error occurred")


line = input()

while line != "End":
    command = line.split("-")[0]
    file_name = line.split("-")[1]
    if command == "Create":
        create_file(file_name)

    elif command == "Add":
        content = line.split("-")[2]
        add_content(file_name, content)

    elif command == "Replace":
        old_str = line.split("-")[2]
        new_str = line.split("-")[3]
        replace_str_in_file(file_name, old_str, new_str)

    elif command == "Delete":
        delete_file(file_name)

    line = input()
