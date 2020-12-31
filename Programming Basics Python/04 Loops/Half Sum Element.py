import sys
n = int(input())

sum = 0
max_number = -sys.maxsize
sum_without_max_number = 0

for i in range(1,n+1):
    input_number = int(input())
    sum += input_number
    if input_number > max_number:
        max_number = input_number
sum_without_max_number = sum - max_number

if max_number == sum_without_max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    print('No')
    print(f'Diff = {abs(max_number - sum_without_max_number)}')


