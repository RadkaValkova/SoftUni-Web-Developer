from project.train.train import Train
import unittest


class TrainTest(unittest.TestCase):
    def setUp(self):
        self.train = Train('asd', 2)

    def test_initialization(self):
        self.assertEqual('asd', self.train.name)
        self.assertEqual(2, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_consants(self):
        self.assertEqual("Train is full", self.train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.train.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.train.PASSENGER_REMOVED)
        self.assertEqual(0, self.train.ZERO_CAPACITY)

    def test_raise_train_full(self):
        self.train.add('B')
        self.train.add('C')
        with self.assertRaises(ValueError):
            self.train.add('A')

    def test_raise_passenger_exist(self):
        self.train.add('B')
        with self.assertRaises(ValueError):
            self.train.add('B')

    def test_add_sucsesfuly(self):
        self.assertEqual("Added passenger A",  self.train.add('A'))

    def test_raise_exc_if_passenger_not_in_train(self):
        self.train.add('A')
        with self.assertRaises(ValueError):
            self.train.remove('B')

    def test_remove(self):
        self.train.add('A')
        self.train.remove('A')
        self.assertEqual([], self.train.passengers)



if __name__ == '__main__':
    unittest.main()

