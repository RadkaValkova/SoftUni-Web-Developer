import math
area = int(input())
grape_per_sqM = float(input())
wine_for_sell = int(input())
workers = int(input())
harvest_grape = area * grape_per_sqM
grape_for_wine = harvest_grape * 0.4
produced_wine = grape_for_wine / 2.5
diference = math.fabs(produced_wine-wine_for_sell)

if produced_wine < wine_for_sell:
    print(f'It will be a tough winter! More {math.floor(diference)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {math.floor(produced_wine)} liters.')
    print(f'{math.ceil(diference)} liters left -> {math.ceil(diference/workers)} liters per person.')


