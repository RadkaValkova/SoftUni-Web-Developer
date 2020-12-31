budget = float(input())
name = ''
is_enough = True
while budget >= 0:
    name = input()
    if name == 'ACTION':
        is_enough = False
        break
    if len(name) > 15:
        pay = budget * 0.2
    else:
        pay = float(input())
    budget -= pay

if is_enough:
    print(f'We need {abs(budget):.2f} leva for our actors.')
else:
    print(f'We are left with {abs(budget):.2f} leva.')
