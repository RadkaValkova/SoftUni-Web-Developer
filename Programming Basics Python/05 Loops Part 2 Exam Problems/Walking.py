sum_steps = 0
is_reached = True
steps_back_home = 0

while sum_steps < 10000:
    steps = input()
    if steps == 'Going home':
        steps_back_home = int(input())
        sum_steps += steps_back_home
        break

    number = int(steps)
    sum_steps += number

if sum_steps < 10000:
    print(f'{abs(10000 - sum_steps)} more steps to reach goal.')
else:
    print('Goal reached! Good job!')
    print(f'{abs(10000-sum_steps)} steps over the goal!')


# goal = 10000
# sum_steps = 0
# while True:
#     line = input()
#
#     if line == 'Going home':
#         line = input()
#         day_steps = int(line)
#         sum_steps += day_steps
#         if sum_steps >= goal:
#             print('Goal reached! Good job!')
#             print(f'{sum_steps - goal} steps over the goal!')
#             break
#         else:
#             print(f'{goal - sum_steps} more steps to reach goal.')
#             break
#
#     day_steps = int(line)
#     sum_steps += day_steps
#
#     if sum_steps >= goal:
#         print('Goal reached! Good job!')
#         print(f'{sum_steps - goal} steps over the goal!')
#         break