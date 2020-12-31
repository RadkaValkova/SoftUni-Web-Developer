import re

text = input()
pattern = r'([@|#])([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1'

matches = re.findall(pattern, text)
mirror_pairs = []
if matches:
    for match in matches:
        if match[1][::-1] == match[2]:

            mirror_pairs.append(match[1])
else:
    print(f'No word pairs found!')

if len(matches) > 0:
    print(f'{len(matches)} word pairs found!')
if len(mirror_pairs) > 0:
    print('The mirror words are:')
    the_print = [f'{mirror_pairs[i]} <=> {mirror_pairs[i][::-1]}' for i in range(len(mirror_pairs))]
    print(', '.join(the_print))

elif len(mirror_pairs) == 0:
    print('No mirror words!')

