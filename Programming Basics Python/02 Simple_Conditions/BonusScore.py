num = int(input())
bonus_score = 0

if num <= 100:
    bonus_score = 5
elif num > 100 and num < 1000:
    bonus_score = num * 0.2
else:
    bonus_score = num * 0.1

if num % 2 == 0:
    bonus_score = bonus_score + 1
if num % 10 == 5:
    bonus_score = bonus_score + 2

print('Bonus points: ' + str(bonus_score))
print('Points with bonus: ' + str(num + bonus_score))