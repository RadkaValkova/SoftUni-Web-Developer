orders_count = int(input())

total = 0

for i in range(orders_count):
    capsule_price = float(input())
    days = int(input())
    capsule_count = int(input())
    total_for_order = ((days * capsule_count) * capsule_price)
    total += total_for_order
    print(f'The price for the coffee is: ${total_for_order:.2f}')

print(f'Total: ${total:.2f}')
