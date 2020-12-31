n = int(input())

for row in range (1, n+1):
    print(' '*(n-row) + '* '*row)

for row in range (1,n):
    print(' '* row + '* '*(n-row))


n = int(input())
space = ' '
star = '*'
for row in range (1, 2*n):
    if row <= n:
        space = n-row
        star = row
        print(' '*space + '* '*star)
    else:
        space = row-n
        star = n*2 - row
        print(' '*space + '* '*star)



