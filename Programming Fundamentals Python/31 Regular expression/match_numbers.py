import re
pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'

numbers = input()
matches = re.finditer(pattern, numbers)

for match in matches:
    print(match.group(0), end=' ')