days_number = int(input())
total_win = 0
total_lose = 0
total_money = 0
for i in range(1,days_number+1):
    win_counter = 0
    lose_counter = 0
    money = 0
    while True:
        line = input()
        if line == 'Finish':
            if win_counter > lose_counter:
                money = money * 1.1
            break
        result = input()
        if result == 'win':
            win_counter += 1
            money += 20
        else:
            lose_counter += 1
    total_money += money
    total_win += win_counter
    total_lose += lose_counter
if total_win > total_lose:
    total_money = total_money * 1.2
    print(f'You won the tournament! Total raised money: {total_money:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_money:.2f}')