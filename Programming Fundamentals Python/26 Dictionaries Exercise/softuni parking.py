def register(users_dict,username,number):
    if username not in users_dict:
        users_dict[username] = number
        print(f'{username} registered {number} successfully')
    elif username in users_dict:
        print(f'ERROR: already registered with plate number {users_dict[username]}')


def unregister(users_dict, username):
    if username not in users_dict:
        print(f'ERROR: user {username} not found')
    else:
        print(f'{username} unregistered successfully')
        users_dict.pop(username)


number_of_commands = int(input())
users_dict = {}

for i in range(number_of_commands):
    line = input().split()
    command = line[0]

    if command == 'register':
        username = line[1]
        number = line[2]
        register(users_dict, username, number)

    elif command == 'unregister':
        username = line[1]
        unregister(users_dict, username)

for key,value in users_dict.items():
    print(f'{key} => {value}')
