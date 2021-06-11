# from Exercises2.Need_for_speed2.project.motorcycle import Motorcycle
from project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)


# rm = CrossMotorcycle(8,1)
# print(rm.fuel)
# print(rm.fuel_consumption)
# rm.drive(1)
# print(rm.fuel)