total_without_taxes = 0

while True:
    line = input()
    if line == 'special' or line == 'regular':
        total_with_taxes = total_without_taxes * 1.2
        if total_with_taxes == 0:
            print('Invalid order!')
            break
        if line == 'special':
            total_with_taxes = total_with_taxes * 0.9
        print('Congratulations you\'ve just bought a new computer!')
        print(f'Price without taxes: {total_without_taxes:.2f}$')
        print(f'Taxes: {total_without_taxes * 0.2:.2f}$')
        print('-' * 11)
        print(f'Total price: {total_with_taxes:.2f}$')
        break

    component_price = float(line)

    if component_price < 0:
        print('Invalid price!')
        continue
    else:
        total_without_taxes += component_price

