# from Exercises2.Need_for_speed2.project.vehicle import Vehicle
from project.vehicle import Vehicle


class Motorcycle(Vehicle):

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)