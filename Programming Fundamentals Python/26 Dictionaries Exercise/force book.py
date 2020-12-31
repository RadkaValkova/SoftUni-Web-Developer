
force_book = {}
all_users = []

while True:
    line = input()
    if line == 'Lumpawaroo':
        break
    if ' | ' in line:
        force_side, force_user = line.split(' | ')
        if force_side not in force_book:
            force_book[force_side] = []
        force_book[force_side].append(force_user)
        all_users.append(force_user)

    elif ' -> ' in line:
        force_user, force_side = line.split(' -> ')
        if force_user not in all_users:
            force_book[force_side].append(force_user)
            print(f'{force_user} joins the {force_side} side!')
        for key,value in force_book.items():
            if force_user in value and key != force_side:
                force_book[key].remove(force_user)
                if force_side not in force_book:
                    force_book[force_side] = force_user
                    all_users.append(force_user)
                else:
                    force_book[force_side].append(force_user)
                    print(f'{force_user} joins the {force_side} side!')

for key,value in sorted(force_book.items(), key= lambda x: (-len(x[1]),x[0])):
    if len(value) > 0:
        print(f'Side: {key}, Members: {len(value)}')
        sorted_value = sorted(value)
        for i in range(len(sorted_value)):
            print(f'! {sorted_value[i]}')