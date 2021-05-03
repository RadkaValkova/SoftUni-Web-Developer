def read_text_as_list(file):
    text = file.readlines()
    return "".join(text).split('\n')


def modify_line(inp_line):
    line = ''
    chars_to_replace = ["-", ",", ".", "!", "?"]
    for char in inp_line:
        if char in chars_to_replace:
            char = '@'
        line += char
    return line


def reverse_line(inp_line):
    reversed_line = []
    for word in inp_line.split():
        reversed_line.insert(0, word)
    return reversed_line


def print_result(line):
    print(" ".join(line))


with open('text.txt', 'r') as file:
    text_as_list = read_text_as_list(file)
    filtered_text = [text_as_list[i] for i in range(len(text_as_list)) if i % 2 == 0]

    for el in filtered_text:
        modified_el = modify_line(el)
        reversed_el = reverse_line(modified_el)
        print_result(reversed_el)