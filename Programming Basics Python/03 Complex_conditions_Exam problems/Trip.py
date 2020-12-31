budget = float(input())
season = input()
costs = 0
destination = ''
accommodation = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        costs = budget * 0.3
        accommodation = 'Camp'
    else:
        costs = budget * 0.7
        accommodation = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        costs = budget * 0.4
        accommodation = 'Camp'
    else:
        costs = budget * 0.8
        accommodation = 'Hotel'
else:
    destination = 'Europe'
    costs = budget * 0.9
    accommodation = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{accommodation} - {costs:.2f}')

