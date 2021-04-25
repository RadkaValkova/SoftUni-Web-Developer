categories = {category: [] for category in input().split(', ')}
n = int(input())

items_count = 0
sum_quality = 0

for i in range(n):
    line = input().split(' - ')
    categories[line[0]].append(line[1])

    parameters = line[2].split(';')
    items_count += int(parameters[0].split(':')[1])
    sum_quality += int(parameters[1].split(':')[1])


print(f'Count of items: {items_count}')
print(f'Average quality: {sum_quality / len(categories):.2f}')
[print(f'{k} -> {", ".join(v)}') for k,v in categories.items()]
