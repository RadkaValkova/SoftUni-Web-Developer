first_string = input()
second_string = input()

while True:
    if first_string not in second_string:
        break
    else:
        second_string = second_string.replace(first_string, '')

print(second_string)