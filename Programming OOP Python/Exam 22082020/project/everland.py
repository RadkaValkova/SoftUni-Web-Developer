class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        result = 0
        for room in self.rooms:
            result += room.expenses + room.room_cost
        return f'Monthly consumption: {result:.2f}$.'

    def pay(self):
        result = ''
        for room in self.rooms:
            room_monthly_cost = room.expenses + room.room_cost
            if room_monthly_cost <= room.budget:
                result += f'{room.family_name} paid {room_monthly_cost:.2f}$ and have {room.budget:.2f}$ left.\n'
                room.budget -= room_monthly_cost
            else:
                self.rooms.remove(room)
                result += f'{room.family_name} does not have enough budget and must leave the hotel.\n'
        return result[:-1]

    def status(self):
        result = ''
        result += f'Total population: {sum([el.members_count for el in self.rooms])}\n'
        for room in self.rooms:
            result += f'{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n'
            for index, child in enumerate(room.children, start=1):
                result += f'--- Child {index} monthly cost: {30*child.cost:.2f}$\n'
            appliances_cost = sum([app.get_monthly_expense() for app in room.appliances])
            result += f'--- Appliances monthly cost: {appliances_cost:.2f}$\n'

        return result[:-1]