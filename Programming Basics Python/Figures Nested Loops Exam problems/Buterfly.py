n = int(input())
row_half = n-2
star = n-2
tire = n-2


for row in range (1, row_half+1):
    if row % 2 != 0:
        print('*'*star + '\\' + ' '+ '/' + '*'*star)
    else:
        print('-'*tire + '\\' + ' '+ '/' + '-'*tire)
print(' '*(star+1) + '@' + ' '*(star+1))

for row in range (1, row_half+1):
    if row % 2 != 0:
        print('*' * star + '/' + ' ' + '\\' + '*' * star)
    else:
        print('-' * tire + '/' + ' ' + '\\' + '-' * tire)
