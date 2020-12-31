flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
plate_eggs = int(input())
yest = int(input())

flour_costs = flour_price * flour_kg
sugar_costs = sugar_kg * flour_price * 0.75
eggs_costs = plate_eggs * flour_price * 1.1
yest_costs = yest * (flour_price * 0.75) * 0.2

total_costs = flour_costs + sugar_costs + eggs_costs + yest_costs
print(f'{total_costs:.2f}')