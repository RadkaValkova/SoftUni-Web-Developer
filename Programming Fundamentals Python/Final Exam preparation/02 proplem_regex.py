import re

n = int(input())

pattern = r'([\w|\W]+)>([0-9]{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1$'

for i in range(n):
    line = input()
    match = re.findall(pattern, line)

    if match:
        password = match[0][1]+match[0][2]+match[0][3]+match[0][4]
        print(f'Password: {password}')
    else:
        print('Try another password!')
