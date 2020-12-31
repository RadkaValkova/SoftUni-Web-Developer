kind = input()
rows = int(input())
col = int(input())
price = 0

if kind == 'Premiere':
    price = 12
elif kind == 'Normal':
    price = 7.5
elif kind == 'Discount':
    price = 5

incoms = rows * col * price
print(f'{incoms:.2f} leva')
