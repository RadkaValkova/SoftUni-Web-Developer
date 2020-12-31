num = float(input())
unit_1 = input()
unit_2 =input()
result = 0

if unit_1 == 'm':
    if unit_2 == 'cm':
        result = num*100
    else:
        result = num*1000
if unit_1 == 'cm':
    if unit_2 == 'm':
        result = num/100
    else:
        result = num*10
if unit_1 == 'mm':
    if unit_2 == 'm':
        result = num / 1000
    else:
        result = num /10
print('%.3f'% result)