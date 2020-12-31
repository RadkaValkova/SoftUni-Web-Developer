budget = float(input())
flour_price_kg = float(input())
pack_eggs_price = flour_price_kg * 0.75
milk_price_l = flour_price_kg * 1.25
cozonac_cost = 1 * pack_eggs_price + 1 * flour_price_kg + 0.25 * milk_price_l

cozonac_counter = 0
colored_eggs = 0
budget_rest = 0

while budget >= cozonac_cost:
    budget -= cozonac_cost
    cozonac_counter += 1
    colored_eggs += 3
    if cozonac_counter % 3 == 0:
        lost_eggs = cozonac_counter - 2
        colored_eggs -= lost_eggs

print(f'You made {cozonac_counter} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')