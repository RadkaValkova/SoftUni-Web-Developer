flower_type = input()
flower_number = int(input())
season = input()

honey = 0

if season == 'Spring':
    if flower_type == 'Sunflower':
        honey = 10
    elif flower_type == 'Daisy':
        honey = 12 * 1.1
    elif flower_type == 'Lavender':
        honey = 12
    elif flower_type == 'Mint':
        honey = 10 * 1.1
elif season == 'Summer':
    if flower_type == 'Sunflower':
        honey = 8
    elif flower_type == 'Daisy':
        honey = 8
    elif flower_type == 'Lavender':
        honey = 8
    elif flower_type == 'Mint':
        honey = 12
    honey = honey * 1.1
elif season == 'Autumn':
    if flower_type == 'Sunflower':
        honey = 12
    elif flower_type == 'Daisy':
        honey = 6
    elif flower_type == 'Lavender':
        honey = 6
    elif flower_type == 'Mint':
        honey = 6
    honey = honey * 0.95
total_honey = flower_number * honey
print(f'Total honey harvested: {total_honey:.2f}')