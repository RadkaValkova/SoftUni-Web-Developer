n = int(input())
odd_sum = 0
even_sum = 0

for num in range (1,n+1):
    input_number = int(input())
    if num % 2 == 0:
        even_sum += input_number
    else:
        odd_sum += input_number

if even_sum == odd_sum:
    print(f'Yes')
    print(f'Sum = {odd_sum}')
else:
    print(f'No')
    print(f'Diff = {abs(even_sum-odd_sum)}')