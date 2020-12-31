n = int(input())
rows_up = n
col = n*4 +3
dots = n
tire = col - (dots*2 +4)
midle_tire = (col-9)//2
dots_doun = 0
tire_doun = col -4

print('.'*(n+1) + '_'*(col-(n+1)*2) + '.'*(n+1))
for rows in range (1, rows_up+1):
    print('.'*dots + '//' + '_'*tire + '\\\\'+'.'*dots)
    dots -=1
    tire +=2
print('//' + '_'* midle_tire + 'STOP!' + '_'*midle_tire + '\\\\')

for row in range (1, n+1):
    print('.'*dots_doun + '\\\\' + '_'*tire_doun + '//' + '.'*dots_doun)
    dots_doun +=1
    tire_doun -=2
