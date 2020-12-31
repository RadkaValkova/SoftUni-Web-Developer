# usernames = input().split(', ')
#
# valid_usernames = []
#
# for user in usernames:
#     if 3 <= len(user) <= 16 and (user.isalnum() or '_' in user or '-' in user):
#         valid_usernames.append(user)
#
# print('\n'.join(valid_usernames))

def is_valid(username):
    if 3 <= len(username) <= 16:
        if username.isalnum() or '-' in username or '_' in username:
            return True


usernames = input().split(', ')

for username in usernames:
    if is_valid(username):
        print(username)