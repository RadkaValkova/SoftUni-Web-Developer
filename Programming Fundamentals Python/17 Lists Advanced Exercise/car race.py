time_needed = list(map(int, input().split()))

finish = len(time_needed) // 2
left_range = time_needed[:finish]
right_range = time_needed[-1:finish:-1]

left_time = 0
right_time = 0
for time in left_range:
    if time == 0:
        left_time *= 0.8
    left_time += time

for time in right_range:
    if time == 0:
        right_time *= 0.8
    right_time += time

if left_time < right_time:
    winner = 'left'
    print(f'The winner is {winner} with total time: {left_time:.1f}')
else:
    winner = 'right'
    print(f'The winner is {winner} with total time: {right_time:1f}')


# left_car = []
# right_car = []
#
# for time in time_needed[:len(time_needed)//2]:
#     if time == 0:
#         current_time = sum(left_car)
#         left_car.append(-(current_time * 0.2))
#     left_car.append(time)
# for time in time_needed[len(time_needed):len(time_needed)//2:-1]:
#     if time == 0:
#         current_time = sum(right_car)
#         right_car.append(-(current_time * 0.2))
#     right_car.append(time)
#
# if sum(left_car) < sum(right_car):
#     winner = 'left'
#     print(f'The winner is {winner} with total time: {sum(left_car):.1f}')
# else:
#     winner = 'right'
#     print(f'The winner is {winner} with total time: {sum(right_car):1f}')
