money = float(input())
year_to_live = int(input())

sum_costs = 0
ivan_age = 18
costs = 0

for year in range(1800, year_to_live + 1):
    if year % 2 == 0:
        sum_costs += 12000
    elif year % 2 != 0:
        sum_costs += 12000 + 50*ivan_age
    ivan_age += 1

if money >= sum_costs:
    print(f'Yes! He will live a carefree life and will have {money - sum_costs:.2f} dollars left.')
else:
    print(f'He will need {sum_costs - money:.2f} dollars to survive.')