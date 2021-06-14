# from Exercises2.Vehicle2.project.project.vehicle import Vehicle
from project.vehicle import Vehicle
import unittest


class VehicleTest(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(10,10)

    def test_initialization(self):
        self.assertEqual(self.vehicle.fuel, 10)
        self.assertEqual(self.vehicle.horse_power, 10)
        self.assertEqual(self.vehicle.capacity, 10)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)

    def test_raise_exc_if_not_enough_fuel_when_drive(self):
        with self.assertRaises(Exception) as exc:
            self.vehicle.drive(100)
        self.assertEqual(str(exc.exception), 'Not enough fuel')

    def test_fuel_decreasing_when_drive(self):
        self.vehicle.drive(1)
        self.assertEqual(self.vehicle.fuel, 8.75)

    def test_raise_exc_when_refuelinf_more_than_capacity(self):
        with self.assertRaises(Exception) as exc:
            self.vehicle.refuel(100)
        self.assertEqual(str(exc.exception), 'Too much fuel')

    def test_fuel_increasing_when_refueling(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(1)
        self.assertEqual(self.vehicle.fuel, 1)

    def test_str_(self):
        self.assertEqual(self.vehicle.__str__(), 'The vehicle has 10 horse power with 10 fuel left and 1.25 fuel consumption')