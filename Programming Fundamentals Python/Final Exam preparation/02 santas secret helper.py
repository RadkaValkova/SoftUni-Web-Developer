import re

key = int(input())
new_messages = []
while True:
    line = input()
    if line == 'end':
        break
    new_message = ''
    for char in line:
        new_char = ord(char)-key
        new_message += chr(new_char)
    new_messages.append(new_message)

pattern = r'@([a-zA-Z]+)[^@\-!>]*!(G|N)!'
valid_matches = {}
for el in new_messages:
    match = re.findall(pattern,el)
    key = match[0][0]
    value = match[0][1]
    valid_matches[key] = value

for key, value in valid_matches.items():
    if value == 'G':
        print(key)
