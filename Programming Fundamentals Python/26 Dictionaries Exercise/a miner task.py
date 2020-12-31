
line = input()
line_dict = {}

while line != 'stop':
    resource = line
    quantity = int(input())
    if resource not in line_dict:
        line_dict[resource] = 0
    line_dict[resource] += quantity
    line = input()

for (key, value) in line_dict.items():
    print(f'{key} -> {value}')
