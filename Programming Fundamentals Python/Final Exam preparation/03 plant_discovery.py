n = int(input())

plants = {}

for i in range(n):
    line = input().split('<->')
    plant = line[0]
    rarity = int(line[1])
    if plant not in plants:
        plants[plant] = {'rarity': 0, 'rating': []}
    plants[plant]['rarity'] = rarity

while True:
    line = input()
    if line == 'Exhibition':
        break
    tokens = line.split(': ')
    command = tokens[0]
    if command == 'Rate':
        plant = tokens[1].split(' - ')[0]
        rating = int(tokens[1].split(' - ')[1])
        if plant not in plants:
            print('error')
        else:
            plants[plant]['rating'].append(rating)

    elif command == 'Update':
        plant = tokens[1].split(' - ')[0]
        new_rarity = int(tokens[1].split(' - ')[1])
        if plant not in plants:
            print('error')
        else:
            plants[plant]['rarity'] = new_rarity

    elif command == 'Reset':
        plant = tokens[1].split(' - ')[0]
        if plant in plants:
            plants[plant]['rating'].clear()
        else:
            print('error')

for key,value in plants.items():
    if len(plants[key]['rating'])> 0:
        average_rating = sum(plants[key]['rating'])/len(plants[key]['rating'])
        plants[key]['rating'] = average_rating
    else:
        plants[key]['rating'] = 0

print('Plants for the exhibition:')
for key,value in sorted(plants.items(), key=lambda x: (-x[1]['rarity'], -x[1]['rating'])):
    print(f'- {key}; Rarity: {plants[key]["rarity"]}; Rating: {plants[key]["rating"]:.2f}')
