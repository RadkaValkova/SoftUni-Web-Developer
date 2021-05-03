import re


def read_text_as_list(file):
    text = file.readlines()
    return "".join(text).split('\n')


def write_on_output_file(file, str_list):
    pattern_letters = r'[A-Za-z]'
    pattern_punctuation = r'[^[A-Za-z\s]'
    for i in range(len(str_list)):
        all_letters = "".join(re.findall(pattern_letters, str_list[i]))
        all_punctuation_marks = "".join(re.findall(pattern_punctuation, str_list[i]))
        file.write(f'Line {i + 1}: '
                          f'{str_list[i]} '
                          f'({len(all_letters)})'
                          f'({len(all_punctuation_marks)})\n')


with open('text.txt', 'r') as read_file:
    lines = read_text_as_list(read_file)
    with open('output1.txt', 'a') as output_file:
        write_on_output_file(output_file, lines)