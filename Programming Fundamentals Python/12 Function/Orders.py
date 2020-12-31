product = input()
quantity = int(input())


def total_price(product: str, quantity: int):
    price = None
    if product == 'coffee':
        price = 1.50
    elif product == 'coke':
        price = 1.40
    elif product == 'water':
        price = 1.00
    elif product == 'snacks':
        price = 2.00
    result = price * quantity
    if price is not None:
        return f'{result:.2f}'


print(total_price(product, quantity))

