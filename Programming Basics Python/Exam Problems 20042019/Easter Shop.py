start_eggs = int(input())

sold_eggs = 0
fill_eggs = 0
available_eggs = start_eggs
while True:
    command = input()
    if command == 'Close':
        print('Store is closed!')
        print(f'{sold_eggs} eggs sold.')
        break
    eggs_number = int(input())
    if command == 'Buy':
        if available_eggs < eggs_number:
            print('Not enough eggs in store!')
            print(f'You can buy only {available_eggs}.')
            break
        else:
            sold_eggs += eggs_number
            available_eggs -= eggs_number

    else:
        fill_eggs += eggs_number
        available_eggs += eggs_number


