budget = float(input())
destination = input()
season = input()
days = int(input())

total_prise = 0

if destination == 'Dubai':
    if season == 'Winter':
        total_prise = days * 45000 * 0.7
    else:
        total_prise = days * 40000 * 0.7
elif destination == 'Sofia':
    if season == 'Winter':
        total_prise = days * 17000 * 1.25
    else:
        total_prise = days * 12500 * 1.25
else:
    if season == 'Winter':
        total_prise = days * 24000
    else:
        total_prise = days * 20250

if budget >= total_prise:
    print(f'The budget for the movie is enough! We have {(budget-total_prise):.2f} leva left!')
else:
    print(f'The director needs {(total_prise - budget):.2f} leva more!')