monay_available = float(input())
sex = input()
age = int(input())
sport = input()

tax = 0

if sex == 'm':
    if sport == 'Gym':
        tax = 42
    elif sport == 'Boxing':
        tax = 41
    elif sport == 'Yoga':
        tax = 45
    elif sport == 'Zumba':
        tax = 34
    elif sport == 'Dances':
        tax = 51
    else:
        tax = 39
else:
    if sport == 'Gym':
        tax = 35
    elif sport == 'Boxing':
        tax = 37
    elif sport == 'Yoga':
        tax = 42
    elif sport == 'Zumba':
        tax = 31
    elif sport == 'Dances':
        tax = 53
    else:
        tax = 37
if age <= 19:
    tax = tax * 0.8

if monay_available >= tax:
    print(f'You purchased a 1 month pass for {sport}.')
else:
    print(f'You don\'t have enough money! You need ${(tax-monay_available):.2f} more.')

