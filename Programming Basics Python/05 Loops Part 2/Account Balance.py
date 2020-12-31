
sum_money = 0
while True:
    money = input()
    if money == 'NoMoreMoney':
        print(f'Total: {sum_money:.2f}')
        break
    if float(money) < 0:
        print('Invalid operation!')
        print(f'Total: {sum_money:.2f}')
        break
    sum_money += float(money)
    print(f'Increase: {float(money):.2f}')
