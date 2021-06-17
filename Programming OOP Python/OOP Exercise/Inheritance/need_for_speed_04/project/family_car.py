# from Inheritance.need_for_speed_04.project.car import Car
# from Inheritance.need_for_speed_04.project.vehicle import Vehicle
from project.car import Car



class FamilyCar(Car):
    DEFAULT_FUEL_CONSUMPTION = Car.DEFAULT_FUEL_CONSUMPTION

    def __init__(self, fuel, horse_power):
        Car.__init__(self, fuel, horse_power)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
