import unittest

from OddNumberGenerator import get_odd_numbers


class OddNumberGeneratorTest(unittest.TestCase):

    def test_odd_numbers_to_three(self):
        result = get_odd_numbers(3)
        self.assertEqual(result, [1, 3])

    def test_odd_numbers_to_seventeen(self):
        result = get_odd_numbers(17)
        self.assertEqual(result, [1, 3, 5, 7, 9, 11, 13, 15, 17])
