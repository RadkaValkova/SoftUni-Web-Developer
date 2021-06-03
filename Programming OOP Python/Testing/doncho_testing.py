

import unittest

def validate_type(value, types):
    if type(value) not in types:
        raise ValueError('numbers should be numbers')


def my_sum(numbers):
    [validate_type(x, [int,float]) for x in numbers]
    return sum(numbers)


class SampleTest(unittest.TestCase):
    def test_my_sum_when_int_expect_to_be_equal(self):
        numbers = [1,2,3,4]
        actual_result = my_sum(numbers)
        expected_result = 10
        self.assertEqual(actual_result, expected_result)

    def test_my_sum_when_float_expect_to_be_equal(self):
        numbers = [1.0,2.0,3.0,4.0]
        actual_result = my_sum(numbers)
        expected_result = 10.0
        self.assertEqual(actual_result, expected_result)

    def test_my_sum_when_string_expect_value_exception(self):
        numbers = ['a', 'b', 'c']
        with self.assertRaises(ValueError) as context:
            my_sum(numbers)


if __name__ == '__main__':
    unittest.main()

class SampleTest2(unittest.TestCase):
    def test_my_sum_when_string_expect_value_exception(self):
        numbers = ['a', 'b', 'c']
        with self.assertRaises(ValueError) as context:
            my_sum(numbers)


