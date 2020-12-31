import re

pattern = r'^>>([a-zA-Z]+)<<([0-9]+\.?[0-9]+)!([0-9]+)$'
total_money = 0
furniture = []
while True:
    line = input()
    if line == 'Purchase':
        break
    matches = re.match(pattern, line)
    if matches:
        name = matches.group(1)
        price = float(matches.group(2))
        quantity = int(matches.group(3))
        furniture.append(name)
        total_money += price*quantity

print('Bought furniture:')
for x in furniture:
    print(x)
print(f'Total money spend: {total_money:.2f}')
