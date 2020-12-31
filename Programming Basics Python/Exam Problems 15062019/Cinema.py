capacity_seats = int(input())
visitors = input()
incomes = 0
is_full = False
while visitors != 'Movie time!':
    if capacity_seats < int(visitors):
        is_full = True
        break
    capacity_seats -= int(visitors)
    incomes += int(visitors) * 5
    if int(visitors) % 3 == 0:
        incomes -= 5
    visitors = input()
if is_full:
    print('The cinema is full.')
else:
    print(f'There are {capacity_seats} seats left in the cinema.')
print(f'Cinema income - {incomes} lv.')