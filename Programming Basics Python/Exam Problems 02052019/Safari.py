flue_price = 2.10
gide = 100

budget = float(input())
flue_litters = float(input())
day = input()

costs = (flue_litters * flue_price) + gide
if day == 'Saturday':
    costs = costs * 0.9
else:
    costs = costs * 0.8

if budget >= costs:
    print(f'Safari time! Money left: {(budget - costs):.2f} lv.')
else:
    print(f'Not enough money! Money needed: {(costs - budget):.2f} lv.')