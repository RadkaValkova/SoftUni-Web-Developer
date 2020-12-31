def price_is_valid(product,price):
    if product == 'Clothes' and price <= 50:
        return True
    elif product == 'Shoes' and price <= 35:
        return True
    elif product == 'Accessories' and price <= 20.50:
        return True


items = input().split('|')
budget = float(input())
boght_items = []

for item in items:
    tokens = item.split('->')
    product = tokens[0]
    price = float(tokens[1])
    if price_is_valid(product,price):
        if price <= budget:
            budget -= price
            boght_items.append(price*1.4)

profit = sum(boght_items) - sum(boght_items)/1.4
for i in range(len(boght_items)):
    print(f'{boght_items[i]:.2f}', end=' ')
print()
print(f'Profit: {profit:.2f}')

if sum(boght_items) + budget >= 150:
    print('Hello, France!')
else:
    print('Time to go.')

