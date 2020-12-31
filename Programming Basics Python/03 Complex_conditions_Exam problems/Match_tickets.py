budget = float(input())
category = input()
people = int(input())
transport = 0
rest = 0

if category == 'VIP':
    price = 499.99
    if people >= 1 and people <= 4:
        transport = budget * 0.75
    elif people >= 5 and people <= 9:
        transport = budget * 0.60
    elif people >= 10 and people <= 24:
        transport = budget * 0.50
    elif people >= 25 and people <= 49:
        transport = budget * 0.40
    elif people >= 50:
        transport = budget * 0.25
if category == 'Normal':
    price = 249.99
    if people >= 1 and people <= 4:
        transport = budget * 0.75
    elif people >= 5 and people <= 9:
        transport = budget * 0.60
    elif people >= 10 and people <= 24:
        transport = budget * 0.50
    elif people >= 25 and people <= 49:
        transport = budget * 0.40
    elif people >= 50:
        transport = budget * 0.25
rest = budget - transport
if rest  >= people * price:
    print(f'Yes! You have {abs(rest-people*price):.2f} leva left.')
else:
    print(f'Not enough money! You need {abs(rest-people*price):.2f} leva.')

