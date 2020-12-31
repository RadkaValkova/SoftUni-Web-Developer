sold_games = int(input())
Hearthstone = 0
Fornite = 0
Overwatch = 0
Others = 0

for i in range(1,sold_games+1):
    current_game = input()
    if current_game == 'Hearthstone':
        Hearthstone += 1
    elif current_game == 'Fornite':
        Fornite += 1
    elif current_game == 'Overwatch':
        Overwatch += 1
    else:
        Others += 1
total = Hearthstone + Fornite + Overwatch + Others
print(f'Hearthstone - {Hearthstone/total*100:.2f}%')
print(f'Fornite - {Fornite/total*100:.2f}%')
print(f'Overwatch - {Overwatch/total*100:.2f}%')
print(f'Others - {Others/total*100:.2f}%')