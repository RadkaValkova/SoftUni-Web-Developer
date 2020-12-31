h = int(input())
w = int(input())
area = h * w

is_finished = True
while area > 0:
    pieses = input()
    if pieses == 'STOP':
        is_finished = False
        break
    area -= int(pieses)
if is_finished:
    print(f'No more cake left! You need {abs(area)} pieces more.')
else:
    print(f'{area} pieces are left.')

# w_cake = int(input())
# l_cake = int(input())
# area_cake = w_cake * l_cake
# sum_pieces = 0
#
# while True:
#     line = input()
#     if line == 'STOP':
#         print(f'{area_cake - sum_pieces} pieces are left.')
#         break
#     pieses = int(line)
#     sum_pieces += pieses
#     if sum_pieces > area_cake:
#         print(f'No more cake left! You need {sum_pieces - area_cake} pieces more.')
#         break