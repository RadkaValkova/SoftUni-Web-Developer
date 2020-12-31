n = int(input())

heroes = {}

for i in range(n):
    line = input().split()
    name = line[0]
    hp = int(line[1])
    mp = int(line[2])
    if name not in heroes:
        heroes[name] = {'hp': 0, 'mp': 0}
    heroes[name]['hp'] += hp
    heroes[name]['mp'] += mp

while True:
    line = input()
    if line == 'End':
        break
    tokens = line.split(' - ')
    command = tokens[0]
    name = tokens[1]
    if command == 'CastSpell':
        mp_needed = int(tokens[2])
        spell_name = tokens[3]
        if heroes[name]['mp'] >= mp_needed:
            heroes[name]['mp'] -= mp_needed
            print(f'{name} has successfully cast {spell_name} and now has {heroes[name]["mp"]} MP!')
        else:
            print(f'{name} does not have enough MP to cast {spell_name}!')
    elif command == 'TakeDamage':
        damage = int(tokens[2])
        attacker = tokens[3]
        heroes[name]['hp'] -= damage
        if heroes[name]['hp'] > 0:
            print(f'{name} was hit for {damage} HP by {attacker} and now has {heroes[name]["hp"]} HP left!')
        else:
            heroes.pop(name)
            print(f'{name} has been killed by {attacker}!')

    elif command == 'Recharge':
        amount = int(tokens[2])
        if heroes[name]['mp'] + amount >= 200:
            print(f'{name} recharged for {200-heroes[name]["mp"]} MP!')
            heroes[name]['mp'] = 200
        else:
            print(f'{name} recharged for {amount} MP!')
            heroes[name]['mp'] += amount

    elif command == 'Heal':
        amount = int(tokens[2])
        if heroes[name]['hp'] + amount >= 100:
            print(f'{name} healed for {100-heroes[name]["hp"]} HP!')
            heroes[name]['hp'] = 100
        else:
            print(f'{name} healed for {amount} HP!')
            heroes[name]['hp'] += amount

for key, value in sorted(heroes.items(), key=lambda x: (-x[1]['hp'], x[0])):
    print(key)
    print(f"  HP: {value['hp']}")
    print(f"  MP: {value['mp']}")