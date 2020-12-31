start_population = int(input())
years = int(input())
born_bees = 0
dayed_bees = 0

for y in range(1, years + 1):
    born_bees = start_population // 10 * 2
    if y % 5 == 0:
        gone_bees = (start_population + born_bees) // 50 * 5
    else:
        gone_bees = 0
    dayed_bees = (start_population + born_bees - gone_bees) // 20 * 2
    start_population = start_population + born_bees - gone_bees - dayed_bees

print(f'Beehive population: {start_population}')