import unittest

from utils import *


class MyTestCase(unittest.TestCase):
    def test_second_max(self):
        self.assertEqual(second_max([4,1,2,3,]), 3)

    def test_second_max2(self):
        self.assertEqual(second_max([4,1,4,2,3]), 3)

    def test_second_max3(self):
        self.assertEqual(second_max([1]), None)

    def test_second_max4(self):
        self.assertEqual(second_max([]), None)

    def test_odd_even_count(self):
        self.assertEqual(odd_even_count([1,2,3,4]), (2, 2))

    def test_odd_even_count2(self):
        self.assertEqual(odd_even_count([1]), (1, 0))

    def test_odd_even_count3(self):
        self.assertEqual(odd_even_count([2]), (0, 1))

    def test_odd_even_count4(self):
        self.assertEqual(odd_even_count([]), (0, 0))


if __name__ == '__main__':
    unittest.main()
