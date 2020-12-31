message = input()

while True:
    line = input()
    if line == 'Decode':
        break
    tokens = line.split('|')
    command = tokens[0]
    if command == 'Move':
        pass
        # number = int(tokens[1])
        # str_to_move = message[:number]
        # message = message.replace(str_to_move, '')
        # message += str_to_move

    elif command == 'Insert':
        index = int(tokens[1])
        value = tokens[2]
        first = message[:index]
        second = message[index:]
        message = first + value + second

    elif command == 'ChangeAll':
        substring = tokens[1]
        replacement = tokens[2]
        message = message.replace(substring,replacement)

print(f'The decrypted message is: {message}')