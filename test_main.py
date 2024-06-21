# test_main.py

import unittest
from main import add

class TestMain(unittest.TestCase):
    def test_add1(self):
        self.assertEqual(add(3, 4), 7)

    def test_add2(self):
        self.assertEqual(add(-1, 1), 0)

    def test_add3(self):
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
