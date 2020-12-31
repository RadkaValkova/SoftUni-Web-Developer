journay_costs = float(input())
months = int(input())

saved_monay = 0

for i in range(1, months + 1):
    if i % 2 != 0 and i != 1:
        saved_monay -= saved_monay * 0.16
    if i % 4 == 0:
        saved_monay += saved_monay * 0.25
    saved_monay += journay_costs * 0.25

if saved_monay >= journay_costs:
    print(f'Bravo! You can go to Disneyland and you will have {(saved_monay - journay_costs):.2f}lv. for souvenirs.')
else:
    print(f'Sorry. You need {(journay_costs - saved_monay):.2f}lv. more.')
