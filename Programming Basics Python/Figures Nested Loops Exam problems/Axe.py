n = int(input())
row = n
middle_row = n//2
col = n*5
tire_outside_left1 = 3*n
tire_inside1 = 0
tire_outside_right1 = col - tire_outside_left1 - tire_inside1 -2

for row in range (1, n+1):
    print('-'*tire_outside_left1 + '*' + '-'*tire_inside1 + '*'+ '-'*tire_outside_right1)
    tire_inside1 += 1
    tire_outside_right1 -=1

for row in range (1, middle_row +1):
    print('*'*(n*3+1) + '-'*(n-1) + '*'+ '-'*(n-1))

tire_out_left2 = n*3
tire_ins2 = n-1
tire_out_right2 = col - tire_out_left2 -tire_ins2 - 2

for row in range (1, (middle_row-1)+1):
    print('-'*tire_out_left2 + '*'+ '-'*tire_ins2 + '*' + '-'*tire_out_right2)
    tire_out_left2 -=1
    tire_ins2 += 2
    tire_out_right2 -=1

midle_stars = 0
right_dashes =0
is_n_even = n % 2 == 0
if is_n_even:
    midle_stars = 2*n-1
    right_dashes = n//2
else:
    midle_stars = 2*n-2
    right_dashes = n//2 +1
left_dashes = col - midle_stars - right_dashes
print('-'*left_dashes + '*'*midle_stars + '-'*right_dashes)
