cakes = int(input())
plate_eggs = int(input())
cookies_kg = int(input())

cakes_costs = cakes * 3.20
eggs_costs = (plate_eggs * 4.35) + (plate_eggs * 12 * 0.15)
cookies_costs = cookies_kg * 5.40

total_costs = cakes_costs + eggs_costs + cookies_costs
print(f'{total_costs:.2f}')