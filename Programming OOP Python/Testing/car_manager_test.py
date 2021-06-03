from Testing.car_manager import Car
import unittest


class CarTests(unittest.TestCase):
    def setUp(self):
        self.car = Car("a", "b", 1, 4)

    def test_constructor(self):
        self.assertEqual(self.car.make, 'a')
        self.assertEqual(self.car.model, 'b')
        self.assertEqual(self.car.fuel_consumption, 1)
        self.assertEqual(self.car.fuel_capacity, 4)

    def test_make_setter(self):
        with self.assertRaises(Exception) as exc:
            self.car.make = ''
        self.assertEqual(str(exc.exception), "Make cannot be null or empty!")

    def test_model_setter(self):
        with self.assertRaises(Exception) as exc:
            self.car.model = ''
        self.assertEqual(str(exc.exception), "Model cannot be null or empty!")

    def test_fuel_consumption_setter(self):
        with self.assertRaises(Exception) as exc:
            self.car.fuel_consumption = -3
        self.assertEqual(str(exc.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_setter(self):
        with self.assertRaises(Exception) as exc:
            self.car.fuel_capacity = -3
        self.assertEqual(str(exc.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount_setter(self):
        with self.assertRaises(Exception) as exc:
            self.car.fuel_amount = -3
        self.assertEqual(str(exc.exception), "Fuel amount cannot be negative!")

    def test_refuel(self):
        with self.assertRaises(Exception) as exc:
            self.car.refuel(-2)
        self.assertEqual(str(exc.exception), "Fuel amount cannot be zero or negative!")
        self.car.refuel(5)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_drive(self):
        self.car.refuel(4)
        with self.assertRaises(Exception) as exc:
            self.car.drive(1000)
        self.assertEqual(str(exc.exception), "You don't have enough fuel to drive!")
        self.car.drive(10)
        self.assertEqual(self.car.fuel_amount, 3.90)


if __name__ == '__main__':
    unittest.main()


# class CarTest(unittest.TestCase):
#     def setUp(self) -> None:
#         self.c = Car(
#             make='ford',
#             model='ka',
#             fuel_consumption=10,
#             fuel_capacity=100
#         )
#
#     def test_init(self):
#         self.assertEqual(self.c.make, 'ford')
#         self.assertEqual(self.c.model, 'ka')
#         self.assertEqual(self.c.fuel_consumption, 10)
#         self.assertEqual(self.c.fuel_capacity, 100)
#         self.assertEqual(self.c.fuel_amount, 0)
#
#     def test_make_setter(self):
#         self.c.make = 'asd'
#         self.assertEqual(self.c.make, 'asd')
#
#     def test_make_invalid_setter(self):
#         with self.assertRaises(Exception) as exc:
#             self.c.make = ''
#         msg = "Make cannot be null or empty!"
#         self.assertEqual(str(exc.exception), msg)
#
#     def test_model_setter(self):
#         self.c.model = 'asd'
#         self.assertEqual(self.c.model, 'asd')
#
#     def test_model_invalid_setter(self):
#         with self.assertRaises(Exception) as exc:
#             self.c.model = ''
#         msg = "Model cannot be null or empty!"
#         self.assertEqual(str(exc.exception), msg)
#
#     def test_fuel_consumption_setter(self):
#         self.c.fuel_consumption = 20
#         self.assertEqual(self.c.fuel_consumption, 20)
#
#     def test_fuel_consumption_invalid_setter_0(self):
#         with self.assertRaises(Exception) as exc:
#             self.c.fuel_consumption = 0
#         msg = "Fuel consumption cannot be zero or negative!"
#         self.assertEqual(str(exc.exception), msg)
#
#     def test_fuel_consumption_invalid_setter_negative(self):
#         with self.assertRaises(Exception) as exc:
#             self.c.fuel_consumption = -1
#         msg = "Fuel consumption cannot be zero or negative!"
#         self.assertEqual(str(exc.exception), msg)
#
#     def test_fuel_capacity_setter(self):
#         self.c.fuel_capacity = 20
#         self.assertEqual(self.c.fuel_capacity, 20)
#
#     def test_fuel_capacity_invalid_setter_0(self):
#         with self.assertRaises(Exception) as exc:
#             self.c.fuel_capacity = 0
#         msg = "Fuel capacity cannot be zero or negative!"
#         self.assertEqual(str(exc.exception), msg)
#
#     def test_fuel_capacity_invalid_setter_negative(self):
#         with self.assertRaises(Exception) as exc:
#             self.c.fuel_capacity = -1
#         msg = "Fuel capacity cannot be zero or negative!"
#         self.assertEqual(str(exc.exception), msg)
#
#     def test_fuel_amount_setter(self):
#         self.c.fuel_amount = 20
#         self.assertEqual(self.c.fuel_amount, 20)
#
#     def test_fuel_amount_setter_0_is_valid(self):
#         self.c.fuel_amount = 0
#         self.assertEqual(self.c.fuel_amount, 0)
#
#     def test_fuel_amount_invalid_setter_negative(self):
#         with self.assertRaises(Exception) as exc:
#             self.c.fuel_amount = -1
#         msg = "Fuel amount cannot be negative!"
#         self.assertEqual(str(exc.exception), msg)
#
#     def test_refuel(self):
#         self.c.refuel(10)
#         self.assertEqual(self.c.fuel_amount, 10)
#
#     def test_refuel_with_more_than_capacity(self):
#         self.c.fuel_amount = 99
#         self.c.refuel(2)
#         self.assertEqual(self.c.fuel_amount, 100)
#
#     def test_refuel_with_0_fill(self):
#         with self.assertRaises(Exception) as exc:
#             self.c.refuel(0)
#         msg = "Fuel amount cannot be zero or negative!"
#         self.assertEqual(str(exc.exception), msg)
#
#     def test_refuel_with_negative_fill(self):
#         with self.assertRaises(Exception) as exc:
#             self.c.refuel(-1)
#         msg = "Fuel amount cannot be zero or negative!"
#         self.assertEqual(str(exc.exception), msg)
#
#     def test_drive(self):
#         self.c.refuel(10)
#         self.c.drive(100)
#         self.assertEqual(self.c.fuel_amount, 0)
#
#     def test_drive_not_enough_fuel(self):
#         self.c.refuel(1)
#         with self.assertRaises(Exception) as exc:
#             self.c.drive(100)
#         msg = "You don't have enough fuel to drive!"
#         self.assertEqual(str(exc.exception), msg)
#
#
# if __name__ == '__main__':
#     unittest.main()