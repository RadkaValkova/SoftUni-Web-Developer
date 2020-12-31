trip_price = float(input())
puzzle_num = int(input())
dolls_num = int(input())
bear_num = int(input())
minion_num = int(input())
truck_num = int(input())

incoms = puzzle_num * 2.6 + dolls_num * 3 + bear_num * 4.10 + minion_num * 8.2 + truck_num * 2
sell_toys_num = puzzle_num + dolls_num + bear_num + minion_num + truck_num

if sell_toys_num >= 50:
    incoms = incoms - incoms * 0.25
else:
    incoms = incoms
rest = incoms - incoms * 0.1

if rest >= trip_price:
    print(f'Yes! {(rest - trip_price):.2f} lv left.')
else:
    print(f'Not enough money! {(trip_price - rest):.2f} lv needed.')