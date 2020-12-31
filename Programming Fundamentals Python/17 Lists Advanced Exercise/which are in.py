first_strings = input().split(', ')
second_strings = input().split(', ')

new_list = []

for word in first_strings:
    for w in second_strings:
        if word in w:
            if word not in new_list:
                new_list.append(word)

print(new_list)

# first_strings = input().split(', ')
# second_strings = input()
#
# new_list = [x for x in first_strings if x in second_strings]
#
# print(new_list)