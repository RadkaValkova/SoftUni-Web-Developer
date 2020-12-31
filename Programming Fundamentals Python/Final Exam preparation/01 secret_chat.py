message = input()


while True:
    line = input()
    if line == 'Reveal':
        break
    tokens = line.split(':|:')
    command = tokens[0]
    if command == 'InsertSpace':
        index = int(tokens[1])
        message = [el for el in message]
        message.insert(index, ' ')
        print(''.join(message))

    elif command == 'Reverse':
        substring = tokens[1]
        if substring in message:
            message = message.replace(substring, '', 1)
            message += substring[::-1]
            print(message)
        else:
            print('error')

    elif command == 'ChangeAll':
        substring = tokens[1]
        replacement = tokens[2]
        message = message.replace(substring, replacement)
        print(message)

print(f'You have a new text message: {"".join(message)}')