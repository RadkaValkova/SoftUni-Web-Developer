n = int(input())
pok = n//2
tire = n*2 - 4 - (n//2)*2

print('/' + '^'*pok + '\\'+ '_'*tire + '/' + '^'*pok + '\\' )
for row in range (1,(n-3) +1):
    print('|' + ' '*(n*2-2) + '|')

print ('|' + ' '*(pok+1) + '_'*tire + ' '*(pok+1) + '|')
print('\\' + '_'*pok + '/'+ ' '*tire + '\\' + '_'*pok + '/' )