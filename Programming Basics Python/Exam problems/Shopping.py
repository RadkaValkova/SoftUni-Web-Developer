budget = float(input())
videocard = int(input())
processors = int(input())
ram = int(input())

videocard_price = 250
processors_price = videocard * videocard_price*0.35
ram_price = videocard * videocard_price*0.1
total_sum = 0
if videocard > processors:
    total_sum = (videocard*videocard_price + processors*processors_price + ram*ram_price)*0.85
else:
    total_sum = videocard*videocard_price + processors*processors_price + ram*ram_price

if budget >= total_sum:
    print(f'You have {(budget-total_sum):.2f} leva left!')
else:
    print(f'Not enough money! You need {(total_sum - budget):.2f} leva more!')
