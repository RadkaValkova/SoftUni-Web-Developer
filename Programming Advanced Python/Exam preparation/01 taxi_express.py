from collections import deque

customers = deque([int(x) for x in input().split(', ')])
taxies = deque([int(x) for x in input().split(', ')])

total_time = 0

while customers:
    current_customer = customers[0]
    if taxies:
        current_taxi = taxies[-1]
    else:
        break
    if current_customer <= current_taxi:
        total_time += current_customer
        customers.popleft()
        taxies.pop()
    else:
        taxies.pop()

if not customers:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
if customers and not taxies:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join([str(el) for el in customers])}')

