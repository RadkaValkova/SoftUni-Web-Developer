destination = input()
dates = input()
nights = int(input())

price = 0
if dates == '21-23':
    if destination == 'France':
        price = 30
    elif destination == 'Italy':
        price = 28
    else:
        price = 32
elif dates == '24-27':
    if destination == 'France':
        price = 35
    elif destination == 'Italy':
        price = 32
    else:
        price = 37
else:
    if destination == 'France':
        price = 40
    elif destination == 'Italy':
        price = 39
    else:
        price = 43
costs = nights * price

print(f'Easter trip to {destination} : {costs:.2f} leva.')