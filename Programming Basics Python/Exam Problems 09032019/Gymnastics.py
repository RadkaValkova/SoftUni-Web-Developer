# •	Първи ред – държава – текст ("Russia", "Bulgaria" или "Italy")
# •	Втори ред – уред - текст ("ribbon", "hoop" или "rope")

country = input()
equipment = input()

points = 0
if country == 'Russia':
    if equipment == 'ribbon':
        points = 9.10 + 9.40
    elif equipment == 'hoop':
        points = 9.30 + 9.80
    else:
        points = 9.60 + 9.00
elif country == 'Bulgaria':
    if equipment == 'ribbon':
        points = 9.60 + 9.40
    elif equipment == 'hoop':
        points = 9.55 + 9.750
    else:
        points = 9.50 + 9.40
else:
    if equipment == 'ribbon':
        points = 9.20 + 9.50
    elif equipment == 'hoop':
        points = 9.450 + 9.350
    else:
        points = 9.70 + 9.15

print(f'The team of {country} get {points:.3f} on {equipment}.')
print(f'{(20-points)/20*100:.2f}%')