round = int(input())
From_0_to_9 = 0
From_10_to_19 = 0
From_20_to_29 = 0
From_30_to_39 = 0
From_40_to_50 = 0
Invalid_numbers = 0
sum_points = 0
for num in range(1,round+1):
    current_num = int(input())
    if 0 <= current_num <= 9:
        From_0_to_9 += 1
        sum_points += current_num * 0.2
    elif 10 <= current_num <= 19:
        From_10_to_19 += 1
        sum_points += current_num * 0.3
    elif 20 <= current_num <= 29:
        From_20_to_29 += 1
        sum_points += current_num * 0.4
    elif 30 <= current_num <= 39:
        From_30_to_39 += 1
        sum_points += 50
    elif 40 <= current_num <= 50:
        From_40_to_50 += 1
        sum_points += 100
    else:
        Invalid_numbers += 1
        sum_points /= 2

print(f'{sum_points:.2f}')
print(f'From 0 to 9: {From_0_to_9/round*100:.2f}%')
print(f'From 10 to 19: {From_10_to_19/round*100:.2f}%')
print(f'From 20 to 29: {From_20_to_29/round*100:.2f}%')
print(f'From 30 to 39: {From_30_to_39/round*100:.2f}%')
print(f'From 40 to 50: {From_40_to_50/round*100:.2f}%')
print(f'Invalid numbers: {Invalid_numbers/round*100:.2f}%')
