import unittest

from project.hardware.hardware import Hardware
from project.software.software import Software


class HardwareTest(unittest.TestCase):
    def setUp(self):
        self.hardware = Hardware('a', 'b', 10, 10)

    def test_initialization(self):
        self.assertEqual(self.hardware.name, 'a')
        self.assertEqual(self.hardware.type, 'b')
        self.assertEqual(self.hardware.capacity, 10)
        self.assertEqual(self.hardware.memory, 10)
        self.assertEqual(self.hardware.software_components, [])

    def test_raise_exception_if_not_memory(self):
        software = Software('a','b',2, 11)
        with self.assertRaises(Exception) as exc:
            self.hardware.install(software)
        self.assertEqual(str(exc.exception), 'Software cannot be installed')

    def test_raise_exception_if_not_capacity(self):
        software = Software('a','b',11, 2)
        with self.assertRaises(Exception) as exc:
            self.hardware.install(software)
        self.assertEqual(str(exc.exception), 'Software cannot be installed')

    def test_append_software_after_installing(self):
        software = Software('a', 'b', 2, 2)
        self.hardware.install(software)
        self.assertEqual(self.hardware.software_components, [software])

    def test_uninstall_software(self):
        software = Software('a', 'b', 2, 2)
        self.hardware.install(software)
        self.hardware.uninstall(software)
        self.assertEqual(self.hardware.software_components, [])

if __name__ == '__main__':
    unittest.main()