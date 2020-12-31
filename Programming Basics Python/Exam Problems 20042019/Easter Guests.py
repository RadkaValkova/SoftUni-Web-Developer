import math
gests = int(input())
budget = int(input())

cakes_num = math.ceil(gests / 3)
eggs_num = gests * 2
total_costs = cakes_num * 4 + eggs_num * 0.45

if budget >= total_costs:
    print(f'Lyubo bought {cakes_num} Easter bread and {eggs_num} eggs.')
    print(f'He has {(budget - total_costs):.2f} lv. left.')
else:
    print('Lyubo doesn\'t have enough money.')
    print(f'He needs {(total_costs - budget):.2f} lv. more.')

