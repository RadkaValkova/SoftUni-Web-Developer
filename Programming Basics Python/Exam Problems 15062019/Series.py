budget = float(input())
series_number = int(input())
total_price = 0

for i in range(1, series_number + 1):
    series_name = input()
    series_price = float(input())
    if series_name == 'Thrones':
        series_price -= series_price * 0.5
    elif series_name == 'Lucifer':
        series_price -= series_price * 0.4
    elif series_name == 'Protector':
        series_price -= series_price * 0.3
    elif series_name == 'TotalDrama':
        series_price -= series_price * 0.2
    elif series_name == 'Area':
        series_price -= series_price * 0.1
    else:
        series_price = series_price
    total_price += series_price
if budget >= total_price:
    print(f'You bought all the series and left with {(budget-total_price):.2f} lv.')
else:
    print(f'You need {(total_price-budget):.2f} lv. more to buy the series!')

