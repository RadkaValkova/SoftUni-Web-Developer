money_for_trip = float(input())
available_money = float(input())

sum_money = available_money
spend_count = 0
day_count = 0

while True:
    command = input()
    day_money = float(input())
    day_count += 1

    if command == 'spend':
        if sum_money <= day_money:
            sum_money = day_money
        sum_money -= day_money
        spend_count += 1

        if spend_count == 5:
            print('You can\'t save the money.')
            print(f'{day_count}')
            break

    else:
        sum_money += day_money
        spend_count = 0

    if sum_money >= money_for_trip:
        print(f'You saved the money for {day_count} days.')
        break