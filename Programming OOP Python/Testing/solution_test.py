from Testing.car_manager import Car
import unittest


class CarTest(unittest.TestCase):
    def setUp(self):
        self.car = Car('ford', 'fiesta', 1, 10)

    def test_initialisation(self):
        self.assertEqual(self.car.make, 'ford')
        self.assertEqual(self.car.model, 'fiesta')
        self.assertEqual(self.car.fuel_consumption, 1)
        self.assertEqual(self.car.fuel_capacity, 10)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_make(self):
        self.assertEqual(self.car.make, 'ford')

    def test_make_setter(self):
        with self.assertRaises(Exception) as exc:
            self.car.make = ''
        self.assertEqual(str(exc.exception), 'Make cannot be null or empty!')

    def test_model(self):
        self.assertEqual(self.car.model, 'fiesta')

    def test_model_setter(self):
        with self.assertRaises(Exception) as exc:
            self.car.model = ''
        self.assertEqual(str(exc.exception), 'Model cannot be null or empty!')

    def test_fuel_consumption(self):
        self.assertEqual(self.car.fuel_consumption, 1)

    def test_fuel_consumption_setter(self):
        test_values = (0,-1)
        for value in test_values:
            with self.assertRaises(Exception) as exc:
                self.car.fuel_consumption = value
            self.assertEqual(str(exc.exception), 'Fuel consumption cannot be zero or negative!')

    def test_fuel_capacity_setter(self):
        test_values = (0,-1)
        for value in test_values:
            with self.assertRaises(Exception) as exc:
                self.car.fuel_capacity = value
            self.assertEqual(str(exc.exception), 'Fuel capacity cannot be zero or negative!')

    def test_fuel_amount_setter(self):
        with self.assertRaises(Exception) as exc:
            self.car.fuel_capacity = -5
        self.assertEqual(str(exc.exception), 'Fuel amount cannot be negative!')

    def test_raise_exc_if_refueling_zero_or_negative(self):
        test_values = (0, -1)
        for value in test_values:
            with self.assertRaises(Exception) as exc:
                self.car.refuel(value)
            self.assertEqual(str(exc.exception), 'Fuel amount cannot be zero or negative!')

    def test_result_after_refueling(self):
        self.car.refuel(1)
        self.assertEqual(self.car.fuel_amount, 1)
        self.car.refuel(100)
        self.assertEqual(self.car.fuel_amount, 10)

    def test_raise_exc_if_not_enough_fuel_to_drive_distance(self):
        with self.assertRaises(Exception) as exc:
            self.car.drive(100)
        self.assertEqual(str(exc.exception), 'You don\'t have enough fuel to drive!')

    def test_fuel_amount_after_driving(self):
        self.car.refuel(10)
        self.car.drive(100)
        self.assertEqual(self.car.fuel_amount, 9)


if __name__ == '__main__':
    unittest.main()
