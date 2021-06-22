from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    def __init__(self, family_name: str, salary: float):
        super().__init__(name=family_name, budget=salary, members_count=1)
        self.room_cost = 10
        self.appliances = [TV()]
        self.expenses = self.calculate_expenses(self.appliances)
        # Calculate the expenses of each appliance.