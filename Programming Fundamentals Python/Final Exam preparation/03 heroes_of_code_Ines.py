def cast_spell(heroes_dict,hero_name, mp_needed, spell_name):
    current_mana_points = heroes_dict[hero_name]['MP']
    if mp_needed > current_mana_points:
        print(f'{hero_name} does not have enough MP to cast {spell_name}!')
    else:
        heroes_dict[hero_name]['MP'] = current_mana_points - mp_needed
        print(f'{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name]["MP"]} MP!')
    return heroes_dict


heroes = {}

n = int(input())

for _ in range(n):
    data = input().split(' ')
    name = data[0]
    hit_points = int(data[1])
    mana_points = int(data[2])
    heroes[name] = {'HP': hit_points, 'MP': mana_points}

command_data = input()
while not command_data == 'End':
    command_data = command_data.split(' - ')
    command = command_data[0]
    if command == 'CastSpell':
        hero_name, mp_needed, spell_name = command_data[1:]
        mp_needed = int(mp_needed)
        heroes = cast_spell(heroes,hero_name, mp_needed, spell_name)

    elif command == 'TakeDamage':
        pass
    elif command == 'Recharge':
        pass
    elif command == 'Heal':
        pass

    command_data = input()