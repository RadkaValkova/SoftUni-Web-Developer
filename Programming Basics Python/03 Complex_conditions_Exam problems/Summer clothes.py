degree = int(input())
moment = input()

Outfit = ''
Shoes = ''

if 10 <= degree <= 18:
    if moment == 'Morning':
        Outfit = 'Sweatshirt'
        Shoes = 'Sneakers'
    elif moment == 'Afternoon':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    else:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
elif 18 < degree <= 24:
    if moment == 'Morning':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif moment == 'Afternoon':
        Outfit = 'T - Shirt'
        Shoes = 'Sandals'
    else:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
else:
    if moment == 'Morning':
        Outfit = 'T - Shirt'
        Shoes = 'Sandals'
    elif moment == 'Afternoon':
        Outfit = 'Swim Suit'
        Shoes = 'Barefoot'
    else:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'

print(f"It's {degree} degrees, get your {Outfit} and {Shoes}.")







