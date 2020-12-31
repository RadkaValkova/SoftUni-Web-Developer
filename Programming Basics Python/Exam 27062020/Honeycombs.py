bees = int(input())
flowers = int(input())

produced_honey = flowers * bees * 0.21
honeycomb = produced_honey // 100
rest = produced_honey % 100

print(f'{honeycomb:.0f} honeycombs filled.')
print(f'{rest:.2f} grams of honey left.')