# from Testing.vehicle.project.project.vehicle import Vehicle
from project.vehicle import Vehicle
import unittest


class VehicleTest(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(10.0, 100.0)

    def test_init(self):
        self.assertEqual(self.vehicle.fuel, 10.0)
        self.assertEqual(self.vehicle.horse_power, 100.0)

    def test_raise_exception_if_no_enough_fuel_to_drive(self):
        with self.assertRaises(Exception) as exc:
            self.vehicle.drive(100)
        self.assertEqual(str(exc.exception), "Not enough fuel")

    def test_fuel_after_drive(self):
        self.vehicle.fuel = 125
        self.vehicle.drive(100)
        self.assertEqual(self.vehicle.fuel, 0)

    def test_refuel(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(10)
        self.assertEqual(self.vehicle.fuel, 10)

    def test_raise_exception_if_fuel_is_to_much(self):
        with self.assertRaises(Exception) as exc:
            self.vehicle.refuel(100)
        self.assertEqual(str(exc.exception), "Too much fuel")

    def test_str_representation(self):
        self.assertEqual(self.vehicle.__str__(), "The vehicle has 100.0 horse power with 10.0 fuel left and 1.25 fuel consumption")


if __name__ == '__main__':
    unittest.main()


