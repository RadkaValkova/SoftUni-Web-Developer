n = 0
phonebook = {}

while True:
    line = input()
    if not line.isdigit():
        (name, number) = line.split('-')
        if name not in phonebook:
            phonebook[name] = number
        else:
            phonebook[name] = number
    else:
        n = int(line)
        break

for _ in range(n):
    name = input()
    if name not in phonebook:
        print(f'Contact {name} does not exist.')
    else:
        print(f'{name} -> {phonebook[name]}')
