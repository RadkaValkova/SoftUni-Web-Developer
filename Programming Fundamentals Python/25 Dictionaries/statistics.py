line = input()

statistics = {}

while line != 'statistics':
    product = line.split(': ')[0]
    quantity = int(line.split(': ')[1])
    if product not in statistics:
        statistics[product] = quantity
    else:
        statistics[product] += quantity

    line = input()

print('Products in stock:')
for product in statistics:
    print(f'- {product}: {statistics[product]}')
print(f'Total Products: {len(statistics)}')
print(f'Total Quantity: {sum(statistics.values())}')