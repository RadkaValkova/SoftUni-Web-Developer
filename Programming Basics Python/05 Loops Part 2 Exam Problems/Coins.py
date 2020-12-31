rest = float(input())
monet_count = 0
rest = rest * 100

while rest > 0:
    monet_count = rest // 200
    rest = rest % 200
    if rest == 0:
        break
    monet_count += rest // 100
    rest = rest % 100
    if rest == 0:
        break
    monet_count += rest // 50
    rest = rest % 50
    if rest == 0:
        break
    monet_count += rest // 20
    rest = rest % 20
    if rest == 0:
        break
    monet_count += rest // 10
    rest = rest % 10
    if rest == 0:
        break
    monet_count += rest // 5
    rest = rest % 5
    if rest == 0:
        break
    monet_count += rest // 2
    rest = rest % 2
    if rest == 0:
        break
    monet_count += rest // 1
    rest = rest % 1
    if rest > 0 and rest < 1:
        break
print(f'{monet_count:.0f}')
