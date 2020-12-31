n = int(input())

is_n_even = n % 2 == 0
range_rows = 0

star = 1
tire_left = (n-1) // 2
tire_middle = n - tire_left*2 - 2
if is_n_even:
    range_rows = n // 2
    star = 2
else:
    range_rows = n//2 +1

for row in range (0, int(range_rows)):
    if row == 0 and n % 2 != 0:
        print('-'*tire_left + '*' + '-'*tire_left)
    else:
        print('-'*tire_left + '*' + '-'*tire_middle + '*' + '-'*tire_left)
    tire_left -=1
    tire_middle += 2
for row in range (0, int(n-range_rows-1)):
       tire_left = row +1
       tire_middle = n - tire_left*2 -2
       print('-'*tire_left + '*' + '-'*tire_middle + '*' + '-'*tire_left)

