lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
sum_costs = 0
shield_counter = 0

for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        sum_costs += helmet_price
    if i % 3 == 0:
        sum_costs += sword_price
    if i % 2 == 0 and i % 3 == 0:
        sum_costs += shield_price
        shield_counter += 1
        if shield_counter % 2 == 0:
            sum_costs += armor_price

print(f'Gladiator expenses: {sum_costs:.2f} aureus')
