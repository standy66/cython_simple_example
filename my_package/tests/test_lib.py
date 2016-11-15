import unittest
from my_package.lib import add

class TestAdd(unittest.TestCase):
    def test_add_zero(self):
        self.assertEqual(add(0, 10), 10)
        self.assertEqual(add(0, -10), -10)

    def test_add(self):
        self.assertEqual(add(10, 20), 30)
