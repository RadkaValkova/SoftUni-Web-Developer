first_string = input()
second_string = input()
new_string = ''

for i in range(0,len(first_string)):
    if first_string[i] == second_string[i]:
        continue
    else:
        new_string = second_string[0:(i+1)] + first_string[(i+1):len(first_string)]
        print(new_string)
# first_string = input()
# second_string = input()
# new_str = first_string
# l=len(first_string)
#
# for i in range (0,l):
#     if new_str[i]==second_string[i]:
#         continue
#     else:
#         new_str =second_string[0:(i+1)]+first_string[(i+1):l]
#         print(new_str)