"""
@author leon on 8/26/18.
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

import unittest
from danny_do_better_exercises.math_utilities import MathUtilities

class TestDivision(unittest.TestCase):
    def setUp(self):
        self.math_utils = MathUtilities()
    
    def test_integer_division(self):
        # Given
        dividend = 20
        divisor = 2
        expected_int = 10
        # When
        actual_int = self.math_utils.divide(dividend, divisor)
        # Then
        self.assertEqual(expected_int, actual_int)
    
    def test_long_division(self):
        # Given
        dividend = 20000000
        divisor = 1000
        expected_long = 20000
        # When
        actual_long = self.math_utils.divide(dividend, divisor)
        # Then
        self.assertEqual(expected_long, actual_long)
    
    def test_float_division(self):
        # Given
        dividend = 7.5
        divisor = 3
        expected_float = 2.50
        # When
        actual_float = self.math_utils.divide(dividend, divisor)
        # Then
        self.assertEqual(expected_float, actual_float)
    
    def test_double_division(self):
        # Given
        dividend = 5.0
        divisor = 4.0
        expected_double = 1.25
        # When
        actual_double = self.math_utils.divide(dividend, divisor)
        # Then
        self.assertEqual(expected_double, actual_double)

if __name__ == '__main__':
    unittest.main()