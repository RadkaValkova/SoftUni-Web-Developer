contests_dict = {}
while True:
    line = input()
    if line == 'end of contests':
        break
    contest, password = line.split(':')
    if contest not in contests_dict:
        contests_dict[contest] = ''
    contests_dict[contest] = password

users_dict = {}
while True:
    line = input()
    if line == 'end of submissions':
        break
    contest, password, username, points = line.split('=>')
    if contest in contests_dict and contests_dict[contest] == password:
        if username not in users_dict:
            users_dict[username] = {}
            if contest not in users_dict[username]:
                users_dict[username][contest] = int(points)
            else:
                if users_dict[username][contest] < int(points):
                    users_dict[username][contest] = int(points)
        else:
            if contest not in users_dict[username]:
                users_dict[username][contest] = int(points)
            else:
                if users_dict[username][contest] < int(points):
                    users_dict[username][contest] = int(points)

max_points = -1000000
max_user = ''

for key,value in users_dict.items():
    user_points = 0
    for k,v in value.items():
        user_points += int(v)
    if user_points > max_points:
        max_points = user_points
        max_user = key

print(f'Best candidate is {max_user} with total {max_points} points.')
print('Ranking:')
for key,value in sorted(users_dict.items(), key= lambda x: x[0]):
    print(key)
    for k,v in sorted(value.items(), key=lambda x: -x[1]):
        print(f'#  {k} -> {v}')

