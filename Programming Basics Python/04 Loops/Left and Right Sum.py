n = int(input())
left_sum = 0
right_sum = 0

for num in range (0,n*2):
    input_number = int(input())
    if num < n:
        left_sum += input_number
    elif num >= n:
        right_sum += input_number

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {abs(left_sum-right_sum)}')