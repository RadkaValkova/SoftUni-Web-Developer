cities_dict = {}

while True:
    line = input()
    if line == 'Sail':
        break
    tokens = line.split('||')
    city = tokens[0]
    population = int(tokens[1])
    gold = int(tokens[2])
    if city not in cities_dict:
        cities_dict[city] = {'population': population, 'gold': gold}
    else:
        cities_dict[city]['population'] += population
        cities_dict[city]['gold'] += gold

while True:
    line = input()
    if line == 'End':
        break
    tokens = line.split('=>')
    command = tokens[0]
    if command == 'Plunder':
        city = tokens[1]
        people = int(tokens[2])
        gold = int(tokens[3])
        if city in cities_dict:
            cities_dict[city]['population'] -= people
            cities_dict[city]['gold'] -= gold
            print(f'{city} plundered! {gold} gold stolen, {people} citizens killed.')
            if cities_dict[city]['population'] <= 0 or cities_dict[city]['gold'] <= 0:
                print(f'{city} has been wiped off the map!')
                cities_dict.pop(city)
    elif command == 'Prosper':
        city = tokens[1]
        gold = int(tokens[2])
        if gold >= 0:
            cities_dict[city]['gold'] += gold
            print(f'{gold} gold added to the city treasury. {city} now has {cities_dict[city]["gold"]} gold.')
        else:
            print(f'Gold added cannot be a negative number!')

if len(cities_dict)> 0:
    print(f'Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:')
    for key,value in sorted(cities_dict.items(), key=lambda x: (-x[1]['gold'],x[0])):
        print(f'{key} -> Population: {value["population"]} citizens, Gold: {value["gold"]} kg')
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')

