n = int(input())

cars = {}

for i in range(n):
    line = input().split('|')
    car = line[0]
    mileage = int(line[1])
    fuel = int(line[2])
    if car not in cars:
        cars[car] = {'mileage': 0, 'fuel': 0}
    cars[car]['mileage'] += mileage
    cars[car]['fuel'] += fuel

while True:
    line = input()
    if line == 'Stop':
        break
    tokens = line.split(' : ')
    command = tokens[0]
    car = tokens[1]
    if command == 'Drive':
        distance = int(tokens[2])
        fuel = int(tokens[3])
        if cars[car]['fuel'] < fuel:
            print('Not enough fuel to make that ride')
        else:
            cars[car]['mileage'] += distance
            cars[car]['fuel'] -= fuel
            print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
            if cars[car]['mileage'] >= 100000:
                print(f'Time to sell the {car}!')
                cars.pop(car) # del cars[car]

    elif command == 'Refuel':
        fuel = int(tokens[2])
        if cars[car]['fuel'] + fuel < 75:
            cars[car]['fuel'] += fuel
            print(f'{car} refueled with {fuel} liters')
        else:
            print(f'{car} refueled with {75-cars[car]["fuel"]} liters')
            cars[car]['fuel'] = 75

    elif command == 'Revert':
        kilometers = int(tokens[2])
        cars[car]['mileage'] -= kilometers
        if cars[car]['mileage'] >= 10000:
            print(f'{car} mileage decreased by {kilometers} kilometers')
        else:
            cars[car]['mileage'] = 10000

for key,value in sorted(cars.items(), key=lambda x: (-x[1]['mileage'],x[0])):
    print(f'{key} -> Mileage: {value["mileage"]} kms, Fuel in the tank: {value["fuel"]} lt.')