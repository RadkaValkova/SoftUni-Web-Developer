move = input()
type_slon = input()
ticket_number = int(input())
incomes = 0

if type_slon == 'normal':
    if move == 'A Star Is Born':
        incomes = ticket_number * 7.50
    elif move == 'Bohemian Rhapsody':
        incomes = ticket_number * 7.35
    elif move == 'Green Book':
        incomes = ticket_number * 8.15
    else:
        incomes = ticket_number * 8.75
elif type_slon == 'luxury':
    if move == 'A Star Is Born':
        incomes = ticket_number * 10.50
    elif move == 'Bohemian Rhapsody':
        incomes = ticket_number * 9.45
    elif move == 'Green Book':
        incomes = ticket_number * 10.25
    else:
        incomes = ticket_number * 11.55
else:
    if move == 'A Star Is Born':
        incomes = ticket_number * 13.50
    elif move == 'Bohemian Rhapsody':
        incomes = ticket_number * 12.75
    elif move == 'Green Book':
        incomes = ticket_number * 13.25
    else:
        incomes = ticket_number * 13.95

print(f'{move} -> {incomes:.2f} lv.')