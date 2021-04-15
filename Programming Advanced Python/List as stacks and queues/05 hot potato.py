from collections import deque

names = input().split(' ')
tosses = int(input())

children = deque()
tosses_counter = 0

for el in names:
    children.append(el)

while children:
    tosses_counter += 1
    person = children.popleft()
    if tosses_counter == tosses:
        if children:
            tosses_counter = 0
            print(f'Removed {person}')
        else:
            print(f'Last is {person}')
    else:
        children.append(person)

from collections import deque

# names = [el for el in input().split()]
# toss = int(input())
#
# kids = deque(el for el in names)
#
# while len(kids) > 1:
#     counter = toss
#     while counter > 0:
#         current_kid = kids.popleft()
#         kids.append(current_kid)
#         counter -= 1
#         if counter == 0:
#             print(f'Removed {current_kid}')
#             kids.pop()
# print(f'Last is {kids.pop()}')