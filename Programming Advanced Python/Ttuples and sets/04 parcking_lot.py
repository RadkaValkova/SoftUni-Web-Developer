cars = int(input())

cars_numbers = set()

for _ in range(cars):
    (command, car) = input().split(', ')
    if command == 'IN':
        cars_numbers.add(car)
    else:
        cars_numbers.remove(car)
if cars_numbers:
    [print(x) for x in cars_numbers]
else:
    print('Parking Lot is Empty')