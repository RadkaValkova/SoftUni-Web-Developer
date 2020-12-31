password = input()

while True:
    line = input()
    if line == 'Done':
        break
    tokens = line.split()
    command = tokens[0]
    if command == 'TakeOdd':
        password = ''.join([password[i] for i in range(len(password)) if i % 2 != 0])
        print(password)

    elif command == 'Cut':
        index = int(tokens[1])
        length = int(tokens[2])
        substring = password[index:index+length]
        password = password.replace(substring, '',1)
        print(password)

    elif command == 'Substitute':
        substring = tokens[1]
        substitute = tokens[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print('Nothing to replace!')

print(f'Your password is: {password}')