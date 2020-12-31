month = input()
nights = int(input())

costs_studio = 0
costs_apartment = 0

if month == 'May' or month == 'October':
    costs_studio = nights * 50
    costs_apartment = nights * 65
    if nights > 14:
        costs_studio = costs_studio * 0.7
        costs_apartment = costs_apartment * 0.9
    elif nights > 7:
        costs_studio = costs_studio * 0.95

elif month == 'June' or month == 'September':
    costs_studio = nights * 75.2
    costs_apartment = nights * 68.70
    if nights > 14:
        costs_studio = costs_studio * 0.8
        costs_apartment = costs_apartment *0.9
else:
    costs_studio = nights * 76
    costs_apartment = nights * 77
    if nights > 14:
        costs_apartment = costs_apartment * 0.9

print(f'Apartment: {costs_apartment:.2f} lv.')
print(f'Studio: {costs_studio:.2f} lv.')
