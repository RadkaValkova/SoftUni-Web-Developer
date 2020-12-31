fruit = input()
size = input()
qountity = int(input())

bill = 0

if size == 'small':
    if fruit == 'Watermelon':
        bill = qountity * 56*2
    elif fruit == 'Mango':
        bill = qountity * 36.66*2
    elif fruit == 'Pineapple':
        bill = qountity * 42.10*2
    else:
        bill = qountity * 20*2
else:
    if fruit == 'Watermelon':
        bill = qountity * 28.70*5
    elif fruit == 'Mango':
        bill = qountity * 19.60*5
    elif fruit == 'Pineapple':
        bill = qountity * 24.80*5
    else:
        bill = qountity * 15.20*5
if bill >=400 and bill <= 1000:
    bill = bill * 0.85
elif bill > 1000:
    bill = bill *0.5
print(f'{(bill):.2f} lv.')

