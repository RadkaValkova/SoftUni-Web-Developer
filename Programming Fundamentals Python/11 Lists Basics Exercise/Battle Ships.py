rows = int(input())
ships = []

counter = 0

for b in range(1, rows + 1):
    string = input().split(" ")
    integers = [int(num) for num in string]
    ships.append(integers)
attacks = input().split(" ")

ships_num = ships

for attack in attacks:
    i = attack.split("-")
    row_searcher = int(i[0])
    place = ships_num[row_searcher]
    col = int(i[1])
    if place[col] > 0:
        place[col] -= 1
        if place[col] == 0:
            counter += 1

print(counter)