import math
volume = int(input())
debit_P1 = int(input())
debit_P2 = int(input())
hours = float(input())
water = hours * debit_P1 + hours * debit_P2

if water <= volume:
    print(f'The pool is {math.trunc (water/volume*100)}% full. '
          f'Pipe 1: {math.trunc((hours * debit_P1)/water*100)}%. '
          f'Pipe 2: {math.trunc((hours * debit_P2)/water*100)}%.')
if water > volume:
    print(f'For {hours} the pool is overflows '
          f'with {water - volume} liters')
