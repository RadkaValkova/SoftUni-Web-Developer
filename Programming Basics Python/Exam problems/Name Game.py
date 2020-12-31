import sys
name = input()
points = 0
max_result = -sys.maxsize
max_name = ''

while name != 'Stop':
    if name == 'Stop':
        break
    points = 0
    for i in range(0, len(name)):
        current_letter = name[i]
        number = ord(current_letter)
        inputed_number = int(input())
        if number == inputed_number:
            points += 10
        else:
            points += 2
    if points >= max_result:
        max_result = points
        max_name = name
    name = input()
print(f'The winner is {max_name} with {max_result} points!')