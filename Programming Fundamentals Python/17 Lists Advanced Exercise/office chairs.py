rooms = int(input())

free_places = []

for i in range(1, rooms + 1):
    current_room = input()
    tokens = current_room.split()
    places = len(tokens[0])
    taken_places = int(tokens[1])
    room_number = i
    if places < taken_places:
        print(f'{taken_places - places} more chairs needed in room {room_number}')
    else:
        chairs = places - taken_places
        free_places.append(chairs)

if len(free_places) == rooms:
    print(f'Game On, {sum(free_places)} free chairs left')
