budget = int(input())
season = input()
number = int(input())
rent = 0

if season == 'Spring':
    rent = 3000
    if number <= 6:
        rent = rent * 0.9
    elif 7 <= number <= 11:
        rent = rent * 0.85
    else:
        rent = rent * 0.75
elif season == 'Summer' or season == 'Autumn':
    rent = 4200
    if number <= 6:
        rent = rent * 0.9
    elif 7 <= number <= 11:
        rent = rent * 0.85
    else:
        rent = rent * 0.75
else:
    rent = 2600
    if number <= 6:
        rent = rent * 0.9
    elif 7 <= number <= 11:
        rent = rent * 0.85
    else:
        rent = rent * 0.75

if number % 2 == 0 and season != 'Autumn':
    rent = rent * 0.95

if budget >= rent:
    print(f'Yes! You have {(budget-rent):.2f} leva left.')
else:
    print(f'Not enough money! You need {(rent-budget):.2f} leva.')



