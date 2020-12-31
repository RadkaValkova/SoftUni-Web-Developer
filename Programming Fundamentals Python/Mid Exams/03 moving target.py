# targets = list(map(int, input().split()))
# задачата дава 80/100 имам друго решение в листове, без функции и там дава 100/100
#
# def shoot(index, power):
#     if index < len(targets):
#         if targets[index] > 0:
#             targets[index] -= power
#             if targets[index] <= 0:
#                 targets.remove(targets[index])
#                 return targets
#     return targets
#
#
# def add(index, value):
#     if index < len(targets):
#         return targets.insert(index, value)
#     else:
#         print('Invalid placement!')
#
#
# def strike(index, radius):
#     left_rad = index - radius
#     right_rad = index + radius
#     if left_rad in range(len(targets)) and right_rad in range(len(targets)):
#         for i in range(left_rad, right_rad + 1):
#             targets.remove(targets[i])
#             targets.insert(i, 0)
#     else:
#         print('Strike missed!')
#
#
# while True:
#     line = input()
#     if line == 'End':
#         print(f'{"|".join(list(map(str, targets)))}')
#         break
#     command, index, value = line.split()
#     index = int(index)
#     value = int(value)
#     if command == 'Shoot':
#         shoot(index, value)
#     elif command == 'Add':
#         add(index, value)
#     elif command == 'Strike':
#         strike(index, value)
#         targets = [x for x in targets if x != 0]

