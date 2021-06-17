# from Inheritance.need_for_speed_04.project.motorcycle import Motorcycle
# from Inheritance.need_for_speed_04.project.vehicle import Vehicle
from project.motorcycle import Motorcycle
from project.vehicle import Vehicle

class CrossMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = Vehicle.DEFAULT_FUEL_CONSUMPTION

    def __init__(self, fuel, horse_power):
        Motorcycle.__init__(self, fuel, horse_power)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION