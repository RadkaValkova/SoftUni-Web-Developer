gests = int(input())
ticket_price = float(input())
budget = float(input())

if gests >= 10 and gests <= 15:
    ticket_price = ticket_price * 0.85
elif gests > 15 and gests <= 20:
    ticket_price = ticket_price * 0.80
elif gests > 20:
    ticket_price =  ticket_price * 0.75

cake_price =  budget * 0.1
total_costs = gests * ticket_price + cake_price
if budget >= total_costs:
    print(f'It is party time! {(budget - total_costs):.2f} leva left.')
else:
    print(f'No party! {(total_costs - budget):.2f} leva needed.')