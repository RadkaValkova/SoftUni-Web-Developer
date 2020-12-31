people = {}

while True:
    line = input()
    if line == 'Results':
        break
    tokens = line.split(':')
    command = tokens[0]
    if command == 'Add':
        name = tokens[1]
        health = int(tokens[2])
        energy = int(tokens[3])
        if name not in people:
            people[name] = {'health':health, 'energy': energy}
        else:
            people[name]['health'] += health

    elif command == 'Attack':
        attacker = tokens[1]
        defender = tokens[2]
        damage = int(tokens[3])
        if attacker in people and defender in people:
            people[defender]['health'] -= damage
            if people[defender]['health'] <= 0:
                del people[defender]
                print(f'{defender} was disqualified!')
            people[attacker]['energy'] -= 1
            if people[attacker]['energy'] <= 0:
                del people[attacker]
                print(f'{attacker} was disqualified!')

    if command == 'Delete':
        username = tokens[1]
        if username in people:
            del people[username]
        if username == 'All':
            people.clear()


print(f'People count: {len(people)}')
for key, value in sorted(people.items(), key= lambda x: (-x[1]["health"],x[0])):
    print(f'{key} - {value["health"]} - {value["energy"]}')