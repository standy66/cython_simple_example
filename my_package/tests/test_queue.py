import unittest
from my_package.queue import Queue

class TestAdd(unittest.TestCase):
    def test_init(self):
        q = Queue()
