n = int(input())

is_n_even = n % 2 == 0
range_rows = 0
star = 1
tire = (n-star)//2
if is_n_even:
    range_rows = n // 2
    star = 2
else:
    range_rows = n//2 +1


for row in range (0, int(range_rows)):
    print('-'*tire + '*'*star + '-'*tire)
    tire -= 1
    star += 2
for row in range (0,int(n-range_rows)):
    print('|' + '*'* (n-2) + '|')

