import re

text = input()

pattern = '\\b[A-Z][a-z]+[ ][A-Z][a-z]+\\b'

names = re.findall(pattern, text)

print(names)