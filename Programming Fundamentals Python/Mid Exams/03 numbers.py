numbers = list(map(int, input().split()))

average = sum(numbers) / len(numbers)
top_numbers = []

for num in numbers:
    if num > average:
        top_numbers.append(num)
sorted_top_numbers = sorted(top_numbers)
reverced_top_numbers = list(map(str, reversed(sorted_top_numbers)))

if len(reverced_top_numbers) >= 5:
    print(' '.join(reverced_top_numbers[:5]))
elif 5 > len(reverced_top_numbers) > 0:
    print(' '.join(reverced_top_numbers))
else:
    print('No')
