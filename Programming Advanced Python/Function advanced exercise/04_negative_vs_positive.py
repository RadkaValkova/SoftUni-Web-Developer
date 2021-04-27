numbers = [int(x) for x in input().split()]

negative = [x for x in numbers if x < 0]
positive = [x for x in numbers if x >= 0]

print(sum(negative))
print(sum(positive))
if abs(sum(negative)) > sum(positive):
    print('The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')