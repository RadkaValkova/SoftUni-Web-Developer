n = int(input())

stars = 2*n
space = n
slash = 2*n - 2

print('*'*stars + ' '*space + '*'*stars)

for row in range (0, n-2):
    if row == (n - 1)//2 - 1:  # това не го разбрах защо?!?!
        print('*'+ '/'*slash + '*' + '|'*n + '*'+ '/'*slash + '*')
    else:
        print('*'+ '/'*slash + '*' + ' '*n + '*'+ '/'*slash + '*')

print('*'*stars + ' '*space + '*'*stars)