import unittest

from project.factory.factory import Factory
from project.factory.paint_factory import PaintFactory


class PaintFactoryTest(unittest.TestCase):
    def setUp(self):
        self.paint_factory = PaintFactory('name', 10)

    def test_is_factory_abstract(self):
        with self.assertRaises(Exception):
            Factory('asd', 10)

    def test_initialization_of_paint_factory(self):
        self.assertEqual('name', self.paint_factory.name)
        self.assertEqual(10, self.paint_factory.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)
        self.assertEqual({}, self.paint_factory.ingredients)

    def test_adding_invalid_type_expect_raise_exception(self):
        with self.assertRaises(TypeError):
            self.paint_factory.add_ingredient('asd', 1)

    def test_adding_invalid_quantity_expect_raise_exception(self):
        with self.assertRaises(ValueError):
            self.paint_factory.add_ingredient('blue', 15)

    def test_adding_valid_type_and_quality(self):
        self.paint_factory.add_ingredient('blue', 1)
        self.assertEqual({'blue': 1}, self.paint_factory.ingredients)

    def test_remove_product_if_it_dont_exist(self):
        with self.assertRaises(KeyError):
            self.paint_factory.remove_ingredient('blue', 2)

    def test_remove_if_quantity_is_bigger(self):
        self.paint_factory.add_ingredient('blue', 5)
        with self.assertRaises(ValueError):
            self.paint_factory.remove_ingredient('blue', 7)

    def test_remove_valid_quantity(self):
        self.paint_factory.add_ingredient('blue', 5)
        self.paint_factory.remove_ingredient('blue', 1)
        self.assertEqual({'blue':4}, self.paint_factory.ingredients)

    def test_propery_products(self):
        self.assertEqual(self.paint_factory.products, self.paint_factory.ingredients)


if __name__ == '__main__':
    unittest.main()



