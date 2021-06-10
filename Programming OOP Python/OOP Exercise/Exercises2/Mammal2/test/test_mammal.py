from Exercises2.Mammal2.project.mammal import Mammal
import unittest

class MammalTest(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal('bil', 'dog', 'wof')

    def test_initialization(self):
        self.assertEqual(self.mammal.name, 'bil')
        self.assertEqual(self.mammal.type, 'dog')
        self.assertEqual(self.mammal.sound, 'wof')

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), 'animals')

    def test_kingdom_as_privet_atribute(self):
        self.assertEqual(self.mammal._Mammal__kingdom, 'animals')

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(), 'bil makes wof')

    def test_info(self):
        self.assertEqual(self.mammal.info(), 'bil is of type dog')