opened_tabs = int(input())
salary = float(input())
sum_discounts = 0

for i in range(1, opened_tabs+1):
    name = input()
    if name == 'Facebook':
        sum_discounts += 150
        if salary <= sum_discounts:
            break
    if name == 'Instagram':
        sum_discounts += 100
        if salary <= sum_discounts:
            break
    if name == 'Reddit':
        sum_discounts += 50
        if salary <= sum_discounts:
            break

if salary <= sum_discounts:
    print('You have lost your salary.')
else:
    print(f'{(salary-sum_discounts):.0f}')