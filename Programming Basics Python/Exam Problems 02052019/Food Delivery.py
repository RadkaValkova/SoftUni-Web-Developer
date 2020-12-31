chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

toyal_menue = chicken_menu*10.35 + fish_menu*12.40 + vegetarian_menu*8.15
desert = toyal_menue*0.2
delivery = 2.50

check = toyal_menue + desert + delivery
print(f'Total: {check:.2f}')