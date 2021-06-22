from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(name=family_name, budget=salary_one+salary_two, members_count=2+len(children))
        self.room_cost = 30
        self.children = list(children)
        self.appliances = self.members_count * [TV(), Fridge(), Laptop()]
        self.expenses = self.calculate_expenses(self.appliances, self.children)

    #Calculate the expenses (appliances and children expenses).

# yc = YoungCoupleWithChildren('n', 2.5, 2.5, 's', 'm')
# print(yc.__dict__)