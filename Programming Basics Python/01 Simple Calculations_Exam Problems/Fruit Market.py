strawberry_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberry_kg = float(input())

raspberries_price = strawberry_price * 0.5
orannges_price = raspberries_price * 0.6
bananas_price = raspberries_price * 0.2

monay = strawberry_kg*strawberry_price + bananas_price*bananas_kg + orannges_price*oranges_kg + raspberries_kg*raspberries_price
print(monay)