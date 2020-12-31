# current_version = input()
# elements = list(map(int, current_version.split('.')))
#
# for i in range(len(elements)):
#     if elements[2] != 9:
#         elements[2] += 1
#         break
#     else:
#         elements[2] = 0
#         if elements[1] != 9:
#             elements[1] += 1
#             break
#         else:
#             elements[1] = 0
#             elements[0] += 1
#         break
# print(f'{elements[0]}.{elements[1]}.{elements[2]}')
new_version = int(''.join(input().split('.'))) + 1
new_version = '.'.join(str(new_version))
print(new_version)