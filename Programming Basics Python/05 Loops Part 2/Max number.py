import sys
max_number = -sys.maxsize
while True:
    number = input()
    if number == 'Stop':
        break
    if int(number) > max_number:
        max_number = int(number)
print(max_number)
