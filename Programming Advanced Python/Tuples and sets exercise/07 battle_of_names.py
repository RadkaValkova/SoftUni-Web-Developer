n = int(input())

odd_set = set()
even_set = set()

for i in range(1, n+1):
    name = input()
    sum_name = sum([ord(x) for x in name])
    value_of_name = int(sum_name / i)
    if value_of_name % 2 == 0:
        even_set.add(value_of_name)
    else:
        odd_set.add(value_of_name)

if sum(odd_set) > sum(even_set):
    result = odd_set - even_set
    print(', '.join([str(el) for el in result]))
elif sum(odd_set) < sum(even_set):
    result = odd_set ^ even_set
    print(', '.join([str(el) for el in result]))
else:
    result = odd_set | even_set
    print(', '.join([str(el) for el in result]))


