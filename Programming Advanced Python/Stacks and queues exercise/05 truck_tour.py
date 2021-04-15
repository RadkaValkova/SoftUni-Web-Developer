from collections import deque

pump_numbers = int(input())
pumps = deque()

for _ in range(pump_numbers):
    pump = [int(x) for x in input().split()]
    pumps.append(pump)

for i in range(pump_numbers):
    is_valid = True
    fuel = 0

    for _ in range(pump_numbers):
        current = pumps.popleft()
        fuel += current[0]-current[1]
        if fuel < 0:
            is_valid = False
        pumps.append(current)

    if is_valid:
        print(i)
        break
    pumps.append(pumps.popleft())