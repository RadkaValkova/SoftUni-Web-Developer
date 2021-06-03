from Testing.cat_solution import Cat
import unittest


# class AssertRaises:
#     def __init__(self, exc):
#         self.__exc = exc
#         self.__exc_info = {}
#
#     def __enter__(self):
#         return self.__exc_info
#
#     def __exit__(self, exc_type, exc_value,exc_tb):
#         if not isinstance(exc_value, self.__exc):
#             raise AssertionError('Exception not raised')

class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat('Tom')

    def test_size_is_increased_after_eating(self):
        old_size = self.cat.size
        self.cat.eat()
        self.assertEqual(self.cat.size - old_size, 1)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_error_is_raised_cat_is_already_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception) as exc:
            self.cat.eat()
        self.assertEqual(str(exc.exception), 'Already fed.')

    def test_error_is_raised_cat_cannot_sleep_if_not_fed(self):
        with self.assertRaises(Exception) as exc:
            self.cat.sleep()
        self.assertEqual(str(exc.exception), 'Cannot sleep while hungry')

    def test_cannot_sleep_after_sleep(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

if __name__ == "__main__":
    unittest.main()






