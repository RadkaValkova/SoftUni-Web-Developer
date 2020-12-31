item = input().split('|')
budget = float(input())

total_profit = 0
turnover = 0
new_prices = []

for i in range(len(item)):
    element = item[i].split('->')
    current_item = element[0]
    price = float(element[1])
    new_price = 0
    profit = 0
    if current_item == 'Clothes':
        if price <= 50 and price <= budget:
            budget -= price
            new_price = float(price * 1.4)
            profit += new_price - price
            total_profit += profit
            new_prices.append(new_price)
        else:
            continue
    elif current_item == 'Shoes':
        if price <= 35 and price <= budget:
            budget -= price
            new_price = float(price * 1.4)
            profit += new_price - price
            total_profit += profit
            new_prices.append(new_price)
        else:
            continue
    else:
        if price <= 20.50 and price <= budget:
            budget -= price
            new_price = float(price * 1.4)
            profit += new_price - price
            total_profit += profit
            new_prices.append(new_price)
        else:
            continue

for i in range(len(new_prices)):
    print(f'{new_prices[i]:.2f}', end=' ')

print()
print(f'Profit: {total_profit:.2f}')

if sum(new_prices) + budget >= 150:
    print('Hello, France!')
else:
    print('Time to go.')
