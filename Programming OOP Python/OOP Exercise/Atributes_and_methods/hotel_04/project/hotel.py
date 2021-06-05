# from hotel_04.project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        name = f'{stars_count} stars Hotel'
        return Hotel(name)

    def get_room_by_number(self, room_number):
        return [el for el in self.rooms if el.number == room_number][0]

    def add_room(self,room):
        self.rooms.append(room)

    def take_room(self,room_number, people):
        room = self.get_room_by_number(room_number)
        result = room.take_room(people)
        if result:
            return result
        self.guests += people

    def free_room(self, room_number):
        room = self.get_room_by_number(room_number)
        result = room.free_room(room_number)
        guests_to_remove = room.guests
        if result:
            return result
        self.guests -= guests_to_remove

    def print_status(self):
        free_rooms = ', '.join(str(el.number) for el in self.rooms if not el.is_taken)
        taken_rooms = ', '.join(str(el.number) for el in self.rooms if el.is_taken)

        print (f'Hotel {self.name} has {self.guests} total guests')
        if free_rooms:
            print(f'Free rooms: {free_rooms}')
        if taken_rooms:
            print(f'Taken rooms: {taken_rooms}')



# hotel = Hotel.from_stars(5)
#
# first_room = Room(1, 3)
# second_room = Room(2, 2)
# third_room = Room(3, 1)
#
# hotel.add_room(first_room)
# hotel.add_room(second_room)
# hotel.add_room(third_room)
#
# hotel.take_room(1, 4)
# hotel.take_room(1, 2)
# hotel.take_room(3, 1)
# hotel.take_room(3, 1)
#
# hotel.print_status()
