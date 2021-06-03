# import unittest
# from Testing.solution import Person
#
#
# class PersonTest(unittest.TestCase):
#     def setUp(self):
#         self.person = Person('Jordan', 'Jambazov', 27)
#
#     def tearDown(self):
#         self.person = None
#
#     def test_person_is_properly_identified(self):
#         self.assertEqual(self.person.first_name, 'Jordan')
#         self.assertEqual(self.person.last_name, 'Jambazov')
#         self.assertEqual(self.person.age, 27)
#
#     def test_full_name_is_the_combination_of_first_and_second_name(self):
#         full_name = self.person.get_full_name()
#         self.assertEqual(full_name, 'Jordan Jambazov')
#
#     def test_get_info(self):
#         full_info = self.person.get_info()
#         self.assertEqual(full_info, 'Jordan Jambazov is 27 years old')
#
#
# if __name__ == '__main__':
#     unittest.main()


from Testing.solution import Worker
from parameterized import parameterized
import unittest

class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker('Rada', 2000, 500)

    def test_is_correct_worker_initialisation(self):
        self.assertEqual(self.worker.name, 'Rada')
        self.assertEqual(self.worker.salary, 2000)
        self.assertEqual(self.worker.energy, 500)

    def test_energy_is_incremented_after_the_rest_method_is_called(self):
        old_energy = self.worker.energy
        self.worker.rest()
        self.assertEqual(self.worker.energy - old_energy, 1)

    # @parameterized.expand([
    #     (-22,),
    #     (-1,),
    #     (-100,),
    #     (-6,),
    #     (0,),
    # ])
    # def test_error_is_raised_if_try_to_work_with_negative_energy(self,energy):
    #     self.worker.energy = energy
    #     with self.assertRaises(Exception):
    #         self.worker.work()

    def test_error_is_raised_if_try_to_work_with_negative_energy(self):
        for energy in (0, -42):
            self.worker.energy = energy
            with self.assertRaises(Exception):
                self.worker.work()

    def test_increasing_of_money_after_salary(self):
        old_money = self.worker.money
        self.worker.work()
        self.assertEqual(self.worker.money-old_money, self.worker.salary)

    def test_energy_decrease_after_work(self):
        old_energy = self.worker.energy
        self.worker.work()
        self.assertEqual(old_energy - self.worker.energy, 1)

    def test_get_info(self):
        self.assertEqual(self.worker.get_info(), 'Rada has saved 0 money.')


if __name__ == '__main__':
    unittest.main()

