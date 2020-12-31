
while True:
    word = input()
    if word == 'end':
        break
    reversed_word = word[::-1]
    print(f'{word} = {reversed_word}')


# def read_until_command(end_command):
#     lines = []
#
#     while True:
#         line = input()
#         if line == end_command:
#             break
#         lines.append(line)
#     return lines

