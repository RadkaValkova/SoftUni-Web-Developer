fire_cells = input().split('#')
water = int(input())
total_fire = 0
list_needed_water = []

for i in range(len(fire_cells)):
    element = fire_cells[i].split(' = ')
    fire_type = element[0]
    needed_water = int(element[1])

    if water >= total_fire:
        if fire_type == 'High':
            if needed_water >= 81 and needed_water <= 125 and water >= needed_water:
                water -= needed_water
                total_fire += needed_water
                list_needed_water.append(needed_water)
            else:
                continue
        elif fire_type == 'Medium':
            if needed_water >= 51 and needed_water <= 80 and water >= needed_water:
                water -= needed_water
                total_fire += needed_water
                list_needed_water.append(needed_water)
            else:
                continue
        else:
            if needed_water >= 1 and needed_water <= 50 and water >= needed_water:
                water -= needed_water
                total_fire += needed_water
                list_needed_water.append(needed_water)
            else:
                continue
    else:
        break
print('Cells:')

for i in range(len(list_needed_water)):
    print(f' - {list_needed_water[i]}')

print(f'Effort: {(total_fire * 0.25):.2f}')
print(f'Total Fire: {int(total_fire)}')
# fires_and_cells = input().split('#')
# water = int(input())
#
# print('Cells:')
# sum_cells = 0
# for i in range(len(fires_and_cells)):
#     element = fires_and_cells[i].split(' = ')
#     type_of_fire = element[0]  # това може и на един ред: type_of_fire, cell = fires_and_cells[i].split(' = ')
#     cell = int(element[1])
#     cell_is_valid = (type_of_fire == 'High' and cell >= 81 and cell <=125) or (type_of_fire == 'Medium'	and cell >= 51 and cell <=80) or (type_of_fire == 'Low' and cell >= 1 and cell <= 50)
#
#     if cell_is_valid and water >= cell:
#         water -= cell
#         sum_cells += cell       # може cell да ги метнем във лист и после да отпечатаме чрез фор цикъл една под друга
#     else:
#         continue
#     print(f' - {cell}')
#
# effort = sum_cells * 0.25
# print(f'Effort: {effort:.2f}')
# print(f'Total Fire: {sum_cells}')