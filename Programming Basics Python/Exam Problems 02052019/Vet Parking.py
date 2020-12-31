days = int(input())
hours = int(input())
total_sum = 0
current_price = 0

for current_day in range(1, days+1):
    day_sum = 0
    for current_hour in range(1, hours+1):
        if current_day % 2 == 0 and current_hour % 2 != 0:
            day_sum += 2.50
        elif current_day % 2 != 0 and current_hour % 2 == 0:
            days += 1.25
        else:
            day_sum += 1
    print(f'Day: {current_day} - {day_sum:.2f} leva')
    total_sum += day_sum
print(f'Total: {total_sum:.2f} leva')
