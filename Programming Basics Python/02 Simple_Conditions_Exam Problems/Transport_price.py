km = int(input())
a = input()
price = 0

if km >= 100:
    price = km * 0.06
elif km >= 20 and km < 100:
    price = km * 0.09
elif a == 'day':
    price = 0.7 + km * 0.79
else:
    price = 0.7 + km * 0.90

print(price)