from collections import deque

liquids = deque([int(el) for el in input().split()])
ingredients = deque([int(el) for el in input().split()])
food_values = {25:'Bread', 50:'Cake', 75:'Pastry', 100:'Fruit Pie'}
result_food_values = {'Bread': 0, 'Cake': 0, 'Pastry': 0, 'Fruit Pie': 0}

are_made = False

while liquids and ingredients:
    current_liquid = liquids[0]
    current_ingredient = ingredients[-1]
    if current_liquid + current_ingredient in food_values:
        result_food_values[food_values[current_liquid + current_ingredient]] += 1
        liquids.popleft()
        ingredients.pop()
    else:
        liquids.popleft()
        ingredients[-1] += 3
    if result_food_values['Bread'] >= 1 and result_food_values['Cake'] >= 1 and result_food_values[
        'Pastry'] >= 1 and result_food_values['Fruit Pie'] >= 1:
        are_made = True
        break

if are_made:
    print('Wohoo! You succeeded in cooking all the food!')
else:
    print('Ugh, what a pity! You didn\'t have enough materials to cook everything.')

if not liquids:
    print('Liquids left: none')
else:
    print(f'Liquids left: {", ".join([str(el) for el in liquids])}')

if not ingredients:
    print('Ingredients left: none')
else:
    print(f'Ingredients left: {", ".join([str(el) for el in reversed(ingredients)])}')

for k,v in sorted(result_food_values.items(),key= lambda x: x[0]):
    print(f'{k}: {v}')

