n = int(input())

print('+ ' + '- '*(n-2) + '+ ')

for row in range (0,n-2):
    print('| ' + '- '*(n-2) + '| ')

print('+ ' + '- '*(n-2) + '+ ')