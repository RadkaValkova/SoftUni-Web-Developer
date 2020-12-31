nylon_quontity = int(input())
paint_quontity = int(input())
thinner_quontity = int(input())
hours = int(input())

nylon_sum = (nylon_quontity + 2)*1.5
paint_sum = (paint_quontity + paint_quontity*0.1)*14.5
thinner_sum = thinner_quontity*5
backs = 0.4
work = hours * (nylon_sum+paint_sum+thinner_sum+backs)*0.3

total_costs = (nylon_sum+paint_sum+thinner_sum+backs+work)
print(f'Total expenses: {total_costs:.2f} lv.')