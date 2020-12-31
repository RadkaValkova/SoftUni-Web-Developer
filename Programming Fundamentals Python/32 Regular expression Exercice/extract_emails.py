import re

pattern = r' (?P<user>[a-zA-Z0-9]+[-\._]*[a-zA-Z0-9]+)@(?P<host>[a-zA-Z]+[-]*[a-zA-Z]+(\.[a-zA-Z]+[-]*[a-zA-Z]+){1,})'

text = input()

matches = re.findall(pattern, text)

for match in matches:
    user = match[0]
    host = match[1]
    print(f'{user}@{host}')