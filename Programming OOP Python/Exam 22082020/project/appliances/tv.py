from project.appliances.appliance import Appliance


class TV(Appliance):
    def __init__(self):
        super().__init__(cost=1.5)

#
# tv = TV()
# print(tv.cost)
# print(tv.get_monthly_expenses())