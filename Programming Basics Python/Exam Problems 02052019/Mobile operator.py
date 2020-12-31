terms = input()
kind = input()
internet = input()
months = int(input())
price = 0

if terms == 'one':
    if kind == 'Small':
        price = 9.98
    elif kind == 'Middle':
        price = 18.99
    elif kind == 'Large':
        price = 25.98
    else:
        price = 35.99
else:
    if kind == 'Small':
        price = 8.58
    elif kind == 'Middle':
        price = 17.09
    elif kind == 'Large':
        price = 23.59
    else:
        price = 31.79

if internet == 'yes':
    if price <= 10:
        price += 5.50
    elif price <= 30:
        price += 4.35
    else:
        price += 3.85

total = months * price

if terms == 'two':
    total = total * 0.9625

print(f'{total:.2f} lv.')
