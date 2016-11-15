import unittest
from my_package import extra_lib

class TestDist(unittest.TestCase):
    def test_dist(self):
        self.assertEqual(extra_lib.dist(1, 2), 5)
