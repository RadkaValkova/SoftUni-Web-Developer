kind = input()
quantity = int(input())
budget = int(input())
price = 0
costs = 0

if kind == 'Roses':
    price = 5
    costs = quantity * price
    if quantity > 80:
        costs = costs * 0.9
elif kind == 'Dahlias':
    price = 3.8
    costs = quantity * price
    if quantity > 90:
        costs = costs * 0.85
elif kind == 'Tulips':
    price = 2.8
    costs = quantity * price
    if quantity > 80:
        costs = costs * 0.85
elif kind == 'Narcissus':
    price = 3
    costs = quantity * price
    if quantity < 120:
        costs = costs * 1.15
elif kind == 'Gladiolus':
    price = 2.5
    costs = quantity * price
    if quantity < 80:
        costs = costs * 1.20

if budget >= costs:
    print(f'Hey, you have a great garden with {quantity} {kind} and {(budget - costs):.2f} leva left.')
else:
    print(f'Not enough money, you need {(costs - budget):.2f} leva more.')


