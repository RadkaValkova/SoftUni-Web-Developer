cake_number = int(input())
max_points = -1000000000
max_baker = ''

for i in range(1, cake_number + 1):
    baker_name = input()
    sum_points = 0
    while True:
        line = input()
        if line == 'Stop':
            print(f'{baker_name} has {sum_points} points.')
            break
        points = int(line)
        sum_points += points
    if sum_points > max_points:
        max_points = sum_points
        max_baker = baker_name
        print(f'{max_baker} is the new number 1!')
print(f'{max_baker} won competition with {max_points} points!')