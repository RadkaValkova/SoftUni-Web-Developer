email = input()

while True:
    line = input()
    if line == 'Complete':
        break
    tokens = line.split(' ')
    command = tokens[0]
    if command == 'Make':
        case = tokens[1]
        if case == 'Upper':
            email = email.upper()
            print(email)
        else:
            email = email.lower()
            print(email)
    elif command == 'GetDomain':
        count = int(tokens[1])
        last_count = email[len(email)-count:]
        print(last_count)

    elif command == 'GetUsername':
        if '@' not in email:
            print(f'The email {email} doesn\'t contain the @ symbol.')
        else:
            substring = ''
            for char in email:
                if char != '@':
                    substring += char
                if char == '@':
                    break
            print(substring)

    elif command == 'Replace':
        character = tokens[1]
        email = email.replace(character, '-')
        print(email)

    elif command == 'Encrypt':
        result = []
        for char in email:
            current_char = ord(char)
            result.append(str(current_char))
        print(' '.join(result))
