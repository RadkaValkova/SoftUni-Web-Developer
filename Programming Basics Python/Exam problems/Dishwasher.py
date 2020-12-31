bottles = int(input())

milliliters = bottles * 750
plates = 0
pots = 0
consumption = 0
washercounter = 0

while milliliters - consumption >= 0:
    dish = input()
    washercounter += 1
    if dish == 'End':
        break
    if washercounter % 3 == 0:
        pots += int(dish)
    else:
        plates += int(dish)

    consumption = plates*5 + pots*15

if milliliters >= consumption:
    print('Detergent was enough!')
    print(f'{plates} dishes and {pots} pots were washed.')
    print(f'Leftover detergent {milliliters-consumption} ml.')
else:
    print(f'Not enough detergent, {consumption-milliliters} ml. more necessary!')