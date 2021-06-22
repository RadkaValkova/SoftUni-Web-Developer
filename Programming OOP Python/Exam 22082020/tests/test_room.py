from project.rooms.room import Room
import unittest


class RoomTest(unittest.TestCase):
    def setUp(self):
        self.room = Room('A', 10.0, 2)

    def test_initialization(self):
        self.assertEqual('A', self.room.family_name)
        self.assertEqual(10.0, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_raise_exception_if_set_expenses_less_than_zero(self):
        with self.assertRaises(Exception) as exc:
            self.room.expenses = -5
        self.assertEqual('Expenses cannot be negative', str(exc.exception))

    def test_calculate_expenses(self):
        pass
