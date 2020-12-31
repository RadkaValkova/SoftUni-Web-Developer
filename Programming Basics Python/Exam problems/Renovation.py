import math
h = int(input())
w = int(input())
windows = int(input())
walls = h * w * 4
area_for_paint = math.ceil(walls - walls * windows/100)
sum_litters = 0

while True:
    line = input()
    if line == 'Tired!':
        print(f'{area_for_paint - sum_litters} quadratic m left.')
        break
    litters = int(line)
    sum_litters += litters
    if area_for_paint < sum_litters:
        print(f'All walls are painted and you have {sum_litters - area_for_paint} l paint left!')
        break
    if area_for_paint == sum_litters:
        print('All walls are painted! Great job, Pesho!')
        break

