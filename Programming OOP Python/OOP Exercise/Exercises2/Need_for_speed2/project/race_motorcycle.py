# from Exercises2.Need_for_speed2.project.motorcycle import Motorcycle
from motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)


# rm = RaceMotorcycle(8,1)
# print(rm.fuel)
# print(rm.fuel_consumption)
# rm.drive(1)
# print(rm.fuel)