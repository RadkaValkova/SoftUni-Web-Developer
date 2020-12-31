import sys
n = int(input())
max_even = -sys.maxsize
min_even = sys.maxsize
max_odd = -sys.maxsize
min_odd = sys.maxsize
even_sum = 0
odd_sum = 0

for num in range (1, n+1):
    input_number = float(input())
    if num % 2 == 0:
        even_sum += input_number
        if input_number > max_even:
            max_even = input_number
        if input_number < min_even:
            min_even = input_number

    elif num % 2 != 0:
        odd_sum += input_number
        if input_number > max_odd:
            max_odd = input_number
        if input_number < min_odd:
            min_odd = input_number


print(f'OddSum={odd_sum:.2f},')
if min_odd != sys.maxsize:
    print(f'OddMin={min_odd:.2f},')
else:
    print(f'OddMin=No,')
if max_odd != -sys.maxsize:
    print(f'OddMax={max_odd:.2f},')
else:
    print(f'OddMax=No,')

print(f'EvenSum={even_sum:.2f},')
if min_even != sys.maxsize:
    print(f'EvenMin={min_even:.2f},')
else:
    print(f'EvenMin=No,')
if max_even != -sys.maxsize:
    print(f'EvenMax={max_even:.2f}')
else:
    print(f'EvenMax=No')






