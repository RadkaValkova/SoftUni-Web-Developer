from Testing.mammal.project.mammal import Mammal
import unittest


class MammalTest(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal('Tom', 'cat', 'miou')

    def test_init(self):
        self.assertEqual(self.mammal.name, 'Tom')
        self.assertEqual(self.mammal.type, 'cat')
        self.assertEqual(self.mammal.sound, 'miou')

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(), 'Tom makes miou')

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), 'animals')

    def test_info(self):
        self.assertEqual(self.mammal.info(), 'Tom is of type cat')



if __name__ == "__main":
    unittest.main()