age = int(input())
washing_machine = float(input())
toy_price = int(input())

sum_money = 0
toy_count = 0
money = 0
brother = 0

for num in range(1,age+1):
    if num % 2 != 0:
        toy_count += 1
    if num % 2 == 0:
        money += 10
        sum_money += money
        brother += 1
total_money = toy_count*toy_price + sum_money - brother

if total_money >= washing_machine:
    print(f'Yes! {(total_money-washing_machine):.2f}')
else:
    print(f'No! {(washing_machine-total_money):.2f}')


