from project.people.child import Child


class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.__expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError('Expenses cannot be negative')
        self.__expenses = value

    def calculate_expenses(self, *args):
        result = 0
        for el in args:
            for x in el:
                if isinstance(x, Child):
                    result += x.cost * 30
                else:
                    result += x.get_monthly_expense()
        self.expenses = result
        return self.expenses

        # Each element of args will be a list (with children or appliances). Calculate the total cost
        # of all elements in the lists and set the expenses attribute to the result

