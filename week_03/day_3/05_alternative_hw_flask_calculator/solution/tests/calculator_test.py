import unittest
from modules.calculator import *

class TestCalculator(unittest.TestCase):

    def test_add_3_and_2_returns_5(self):
        result = add(2,3)
        self.assertEqual(5, result)


    def test_subtract_2_from_3_returns_1(self):
        result = subtract(3,2)
        self.assertEqual(1, result)


    def test_multiply_3_and_2_returns_6(self):
        result = multiply(3,2)
        self.assertEqual(6, result)


    def test_divide_3_by_2_returns_1_5(self):
        result = divide(3,2)
        self.assertEqual(1.5, result)
