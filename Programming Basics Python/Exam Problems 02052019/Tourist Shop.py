budget = float(input())
product_count = 0
costs = 0
while True:
    product_name = input()

    if product_name == 'Stop':
        print(f'You bought {product_count} products for {costs:.2f} leva.')
        break

    product_price = float(input())
    product_count += 1
    if product_count % 3 == 0:
        product_price = product_price / 2

    if product_price > abs(budget - costs):
        print('You don\'t have enough money!')
        print(f'You need {(product_price - abs(budget - costs)):.2f} leva!')
        break

    costs += product_price