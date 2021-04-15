from collections import deque

food_quantity = int(input())
orders = deque()
line = input().split(' ')

for i in range(len(line)):
    orders.append(int(line[i]))

print(max(orders))
is_complete = True

while orders:
    current_order = orders.popleft()
    if food_quantity >= current_order:
        food_quantity -= current_order
    else:
        is_complete = False
        orders.appendleft(current_order)
        break

if is_complete:
    print('Orders complete')
else:
    print(f'Orders left: {" ".join([str(x) for x in orders])}')
