month = int(input())
electricity = 0
others = 0
sum_costs = 0
water = 0
internet = 0

for i in range(1,month+1):
    current_electricity = float(input())
    electricity += current_electricity
    water += 20
    internet += 15
    others = (electricity + water + internet) * 1.2
    sum_costs = (electricity + water + internet + others)

print(f'Electricity: {electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {others:.2f} lv')
print(f'Average: {sum_costs/month:.2f} lv')