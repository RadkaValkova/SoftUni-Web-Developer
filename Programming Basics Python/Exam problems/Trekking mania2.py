groups_number = int(input())

Musla = 0
Monblan = 0
Kilimanjaro = 0
K2 = 0
Everest = 0
all = 0

for i in range(1, groups_number + 1):
    tourists_in_group = int(input())
    all += tourists_in_group
    if tourists_in_group <= 5:
        Musla += tourists_in_group
    elif tourists_in_group >= 6 and tourists_in_group <=12:
        Monblan += tourists_in_group
    elif tourists_in_group >= 13 and tourists_in_group <= 25:
        Kilimanjaro += tourists_in_group
    elif tourists_in_group >=26 and tourists_in_group <=40:
        K2 += tourists_in_group
    elif tourists_in_group >= 41:
        Everest += tourists_in_group

print(f'{Musla/all*100:.2f}%')
print(f'{Monblan/all*100:.2f}%')
print(f'{Kilimanjaro/all*100:.2f}%')
print(f'{K2/all*100:.2f}%')
print(f'{Everest/all*100:.2f}%')
