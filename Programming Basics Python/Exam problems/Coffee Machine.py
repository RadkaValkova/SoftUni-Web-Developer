drink_type = input()
sugar = input()
number = int(input())
price = 0


if drink_type == 'Espresso':
    if sugar == 'Without':
        price = 0.90
    elif sugar == 'Normal':
        price = 1
    else:
        price = 1.20
elif drink_type == 'Cappuccino':
    if sugar == 'Without':
        price = 1
    elif sugar == 'Normal':
        price = 1.20
    else:
        price = 1.60
elif drink_type == 'Tea':
    if sugar == 'Without':
        price = 0.50
    elif sugar == 'Normal':
        price = 0.60
    else:
        price = 0.70
total = number * price
if sugar == 'Without':
    total = total*0.65
if drink_type == 'Espresso' and number >= 5:
    total = total*0.75
if total > 15:
    total = total*0.8
print(f'You bought {number} cups of {drink_type} for {total:.2f} lv.')