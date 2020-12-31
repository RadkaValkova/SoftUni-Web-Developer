rent = int(input())
statuettes = rent * 0.7
food = statuettes * 0.85
sound = food * 0.5

total_costs = rent + statuettes + food + sound
print(f'{total_costs:.2f}')