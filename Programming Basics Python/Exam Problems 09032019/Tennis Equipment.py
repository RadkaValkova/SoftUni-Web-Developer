import math
tennis_racket_price = float(input())
tennis_racket_number = int(input())
shoes_number = int(input())

rackets_total = tennis_racket_number * tennis_racket_price
shoes_total = shoes_number * tennis_racket_price*1/6
others = (rackets_total+shoes_total)*0.2
total = rackets_total + shoes_total + others

print(f'Price to be paid by Djokovic {math.floor (1/8 * total )}')
print(f'Price to be paid by sponsors {math.ceil(7/8 * total)}')