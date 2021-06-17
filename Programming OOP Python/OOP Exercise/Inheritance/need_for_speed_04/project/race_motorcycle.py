# from Inheritance.need_for_speed_04.project.motorcycle import Motorcycle
from project.motorcycle import Motorcycle

class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    def __init__(self, fuel, horse_power):
        Motorcycle.__init__(self, fuel, horse_power)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
