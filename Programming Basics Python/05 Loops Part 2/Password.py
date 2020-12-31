username = input()
password = input()

input_password = ''
while input_password != password:
    input_password = input()

print(f'Welcome {username}!')