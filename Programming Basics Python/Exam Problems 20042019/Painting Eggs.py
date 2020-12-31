size = input()
color = input()
series = int(input())
price = 0

if color == 'Red':
    if size == 'Large':
        price = 16
    elif size == 'Medium':
        price = 13
    else:
        price = 9
elif color == 'Green':
    if size == 'Large':
        price = 12
    elif size == 'Medium':
        price = 9
    else:
        price = 8
else:
    if size == 'Large':
        price = 9
    elif size == 'Medium':
        price = 7
    else:
        price = 5
incomes = series * price
net_incomes = incomes * 0.65
print(f'{net_incomes:.2f} leva.')