year_tax = int(input())
shoes = year_tax * 0.6
clothes = shoes * 0.8
ball = clothes * 1 / 4
accessories = ball * 1 / 5

total_price = year_tax + shoes + clothes + ball + accessories
print(f'{total_price:.2f}')
