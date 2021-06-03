from Testing.extended_list import IntegerList
import unittest


class ExtendedListTest(unittest.TestCase):
    def setUp(self):
        self.list = IntegerList([])

    def test_add(self):
        self.assertEqual(self.list.add(42), [42])

    def test_raise_error_if_element_added_is_not_int(self):
        # with self.assertRaises(Exception) as exc:
        #     self.list.add(2.5)
        # self.assertEqual(str(exc.exception), "Element is not Integer")
        self.assertRaises(ValueError, self.list.add, 'baba')
        # with self.assertRaises(ValueError): това е идентично с горния ред
        #     self.list.add(2.5)

    def test_remove_by_index(self):
        self.list.add(42)
        el = self.list.remove_index(0)
        self.assertEqual(el, 42)

    def test_raise_error_if_index_is_invalid_when_remove_element(self):
        # with self.assertRaises(Exception) as exc:
        #     self.list.remove_index(1)
        # self.assertEqual(str(exc.exception), "Index is out of range")
        self.assertRaises(IndexError, self.list.remove_index, 0)

    def test_init_takes_only_int(self):
        list = IntegerList('b', 12, 't')
        self.assertEqual(list.get_data(), [12])

    def test_get(self):
        self.list.add(12)
        self.assertEqual(self.list.get(0), 12)

    def test_if_raise_error_when_get_element_out_of_range(self):
        # with self.assertRaises(Exception) as exc:
        #     self.list.get(0)
        # self.assertEqual(str(exc.exception), "Index is out of range")
        self.assertRaises(IndexError, self.list.get, 0)

    def test_insert(self):
        self.assertRaises(IndexError, self.list.insert, 0,42)
        self.list.add(1)
        self.assertRaises(ValueError, self.list.insert, 0,'baba')
        self.list.insert(0, 42)
        self.assertEqual(self.list.get_data(), [42,1])

    def test_get_biggest(self):
        self.list.add(1)
        self.list.add(3)
        self.list.add(5)
        self.assertEqual(self.list.get_biggest(), 5)

    def test_get_index(self):
        self.list.add(1)
        self.assertEqual(self.list.get_index(1), 0)


if __name__ == "__main__":
    unittest.main()
