budget = float(input())
statists = int(input())
price_for_clotes_for_1 = float(input())

decor = budget*0.1
clotes = statists * price_for_clotes_for_1

if statists > 150:
    clotes = clotes *0.9

costs = decor + clotes
if costs > budget:
    print('Not enough money!')
    print(f'Wingard needs {costs-budget:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {budget-costs:.2f} leva left.')