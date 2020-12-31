movie = input()
type_ticket = input()
ticket_number = int(input())

total_price = 0

if movie == 'John Wick':
    if type_ticket == 'Drink':
        total_price = ticket_number * 12
    elif type_ticket == 'Popcorn':
        total_price = ticket_number * 15
    else:
        total_price = ticket_number * 19
elif movie == 'Star Wars':
    if type_ticket == 'Drink':
        total_price = ticket_number * 18
    elif type_ticket == 'Popcorn':
        total_price = ticket_number * 25
    else:
        total_price = ticket_number * 30
    if ticket_number >= 4:
        total_price = total_price * 0.7
else:
    if type_ticket == 'Drink':
        total_price = ticket_number * 9
    elif type_ticket == 'Popcorn':
        total_price = ticket_number * 11
    else:
        total_price = ticket_number * 14
    if ticket_number == 2:
        total_price = total_price * 0.85

print(f'Your bill is {total_price:.2f} leva.')