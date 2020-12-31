stage = input()
ticket_type = input()
ticket_number = int(input())
trophy_picture = input()

price = 0
if stage == 'Quarter final':
    if ticket_type == 'Standard':
        price = 55.50 * ticket_number
    elif ticket_type == 'Premium':
        price = 105.20 * ticket_number
    else:
        price = 118.90 * ticket_number
elif stage == 'Semi final':
    if ticket_type == 'Standard':
        price = 75.88 * ticket_number
    elif ticket_type == 'Premium':
        price = 125.22 * ticket_number
    else:
        price = 300.40 * ticket_number
else:
    if ticket_type == 'Standard':
        price = 110.10 * ticket_number
    elif ticket_type == 'Premium':
        price = 160.66 * ticket_number
    else:
        price = 400 * ticket_number
if trophy_picture == 'Y':
    if price > 4000:
        price = price * 0.75
    elif price > 2500:
        price = price * 0.9 + (ticket_number * 40)
    else:
        price = price + (ticket_number * 40)
else:
    if price > 4000:
        price = price * 0.75
    elif price > 2500:
        price = price * 0.9
    else:
        price = price
print(f'{price:.2f}')