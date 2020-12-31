def legendary_item(material):
    result = None
    if material == 'shards':
        result = 'Shadowmourne'
    elif material == 'fragments':
        result = 'Valanyr'
    elif material == 'motes':
        result = 'Dragonwrath'
    return result


is_obtained = False

materials_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
others_dict = {}

while not is_obtained:
    materials = input().lower().split()
    for i in range(0, len(materials), 2):
        quantity = int(materials[i])
        key_material = materials[i+1]
        if key_material in materials_dict:
            materials_dict[key_material] += quantity
            if materials_dict[key_material] >= 250:
                materials_dict[key_material] -= 250
                is_obtained = True
                print(f'{legendary_item(key_material)} obtained!')
                break
        else:
            if key_material not in others_dict:
                others_dict[key_material] = 0
            others_dict[key_material] += quantity

for key,value in sorted(materials_dict.items(), key=lambda x: (-x[1],x[0])):
    print(f'{key}: {value}')

for (key, value) in sorted(others_dict.items()):
    print(f'{key}: {value}')

