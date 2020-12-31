# import re
#
# line = input()
# pattern = r'([^0-9]+)([0-9]+)'
#
# matches = re.findall(pattern, line)
# result = ''
# unique_symbols = set()
#
# for match in matches:
#     str_to_repeat = match[0].upper()
#     num_to_repeat = int(match[1])
#     result += f'{str_to_repeat * num_to_repeat}'
#     for i in range(len(str_to_repeat)):
#         unique_symbols.add(str_to_repeat[i])
#
# print(f'Unique symbols used: {len(unique_symbols)}')
# print(result)

line = input()
current_result = ''
result = ''
index = 0
for i in range(len(line)):
    if not line[i].isdigit():
        current_result += line[i]
    else:
        number = ''
        while line[i].isdigit():
            number += line[i]
            if i + 1 < len(line):
                i = i+1
            else:
                break
        current_result = current_result.upper() * int(number)
        result += current_result
        current_result = ''

print(f'Unique symbols used: {len(set(result))}')
print(result)

