products_dict = {}

while True:
    line = input()
    if line == 'buy':
        break
    product = line.split()[0]
    price = line.split()[1]
    quantity = line.split()[2]

    if product not in products_dict:
        products_dict[product] = {'price': float(price), 'quantity': int(quantity)}
    else:
        products_dict[product]['price'] = float(price)
        products_dict[product]['quantity'] += int(quantity)

for key,value in products_dict.items():
    total = value['price'] * value['quantity']
    print(f'{key} -> {total:.2f}')