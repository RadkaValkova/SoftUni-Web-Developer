import math
companion_number = int(input())
days = int(input())
sum_coins = 0

for i in range(1, days+1):
    if i % 10 == 0:
        companion_number -= 2
    if i % 15 == 0:
        companion_number += 5
    sum_coins += 50
    sum_coins -= companion_number * 2
    if i % 3 == 0:
        sum_coins -= companion_number * 3
    if i % 5 == 0:
        sum_coins += companion_number * 20
        if i % 3 == 0:
            sum_coins -= companion_number * 2

print(f'{companion_number} companions received {math.floor(sum_coins/companion_number)} coins each.')