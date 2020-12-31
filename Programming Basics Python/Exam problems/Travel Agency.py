town = input()
type_package = input()             # дава 75 от 100
vip = input()
days = int(input())

price = 0
if days > 7:
    days -= 1
if (town != 'Bansko'and town !='Borovets'and town !='Varna'and town !='Burgas') or (type_package != 'noEquipment'and type_package !='withEquipment'and type_package !='noBreakfast'and type_package !='withBreakfast'):
    print('Invalid input!')
elif days <= 0:
    print('Days must be positive number!')
else:
    if town == 'Bansko' or town == 'Borovets':
        if type_package == 'withEquipment':
            price = 100
            if vip == 'yes':
                price = price*0.9
            elif vip == 'no':
                price = price
        elif type_package == 'noEquipment':
            price = 80
            if vip == 'yes':
                price = price*0.95
            elif vip == 'no':
                price = price
    elif town == 'Varna' or town == 'Burgas':
        if type_package == 'withBreakfast':
            price = 130
            if vip == 'yes':
                price = price*0.88
            elif vip == 'no':
                price = price
        elif type_package == 'noBreakfast':
            price = 100
            if vip == 'yes':
                price = price*0.93
            elif vip == 'no':
                price = price
    stay_sum = days * price
    print(f'The price is {stay_sum:.2f}lv! Have a nice time!')
