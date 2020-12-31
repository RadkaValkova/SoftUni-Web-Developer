last_sector = input()
rows_first_sector = int(input())
seats_odd_row = int(input())
row_seats = seats_odd_row
seats_counter = 0

for sector in range(ord('A'), ord(last_sector)+1):
    rows_first_sector += 1
    for row in range(1, rows_first_sector):
        if row % 2 == 0:
            row_seats = seats_odd_row + 2
        else:
            row_seats = seats_odd_row
        for seats in range(97, 97 + row_seats):
            seats_counter += 1

            print(f'{chr(sector)}{row}{chr(seats)}')
print(seats_counter)