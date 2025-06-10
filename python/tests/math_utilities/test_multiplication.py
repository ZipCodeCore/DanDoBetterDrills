"""
@author leon on 8/26/18.
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

import unittest
from danny_do_better_exercises.math_utilities import MathUtilities

class TestMultiplication(unittest.TestCase):
    def setUp(self):
        self.math_utils = MathUtilities()
    
    def test_integer_multiplication(self):
        # Given
        multiplicand = 5
        multiplier = 2
        expected_int = 10
        # When
        actual_int = self.math_utils.multiply(multiplicand, multiplier)
        # Then
        self.assertEqual(expected_int, actual_int)
    
    def test_long_multiplication(self):
        # Given
        multiplicand = 20
        multiplier = 1000
        expected_long = 20000
        # When
        actual_long = self.math_utils.multiply(multiplicand, multiplier)
        # Then
        self.assertEqual(expected_long, actual_long)
    
    def test_float_multiplication(self):
        # Given
        multiplicand = 2.5
        multiplier = 1
        expected_float = 2.50
        # When
        actual_float = self.math_utils.multiply(multiplicand, multiplier)
        # Then
        self.assertEqual(expected_float, actual_float)
    
    def test_double_multiplication(self):
        # Given
        multiplicand = 3.25
        multiplier = 3.0
        expected_double = 9.75
        # When
        actual_double = self.math_utils.multiply(multiplicand, multiplier)
        # Then
        self.assertEqual(expected_double, actual_double)

if __name__ == '__main__':
    unittest.main()