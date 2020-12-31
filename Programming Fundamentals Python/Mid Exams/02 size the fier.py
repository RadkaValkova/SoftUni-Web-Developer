def cell_is_valid(type,value):
    if type == 'High' and value >= 81 and value <= 125:
        return True
    elif type == 'Medium' and value >= 51 and value <= 80:
        return True
    elif type == 'Low' and value >= 1 and value <= 50:
        return True


cells = input().split('#')
water = int(input())
effort = 0
total_fire = 0
print('Cells:')
for i in range(len(cells)):
    if water <= 0:
        break
    tokens = cells[i].split(' = ')
    fire_type = tokens[0]
    needed_water = int(tokens[1])
    if cell_is_valid(fire_type,needed_water):
        if water >= needed_water:
            water -= needed_water
            effort += needed_water * 0.25
            total_fire += needed_water
            print(f' - {needed_water}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')