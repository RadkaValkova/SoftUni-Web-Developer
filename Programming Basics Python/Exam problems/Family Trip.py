budget = float(input())
nights = int(input())
price_per_night = float(input())
add_costs_percent = int(input())
sum_nights = 0
add_costs = budget*add_costs_percent/100

if nights <= 7:
    sum_nights = nights * price_per_night
else:
    sum_nights = nights * price_per_night*0.95
total_costs = sum_nights+add_costs

if budget >= total_costs:
    print(f'Ivanovi will be left with {(budget-total_costs):.2f} leva after vacation.')
else:
    print(f'{(total_costs-budget):.2f} leva needed.')