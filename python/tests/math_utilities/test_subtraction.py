"""
@author leon on 8/26/18.
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

import unittest
from danny_do_better_exercises.math_utilities import MathUtilities

class TestSubtraction(unittest.TestCase):
    def setUp(self):
        self.math_utils = MathUtilities()
    
    def test_integer_subtraction(self):
        # Given
        base_value = 20
        difference = 7
        expected_int = 13
        # When
        actual_int = self.math_utils.subtract(base_value, difference)
        # Then
        self.assertEqual(expected_int, actual_int)
    
    def test_long_subtraction(self):
        # Given
        base_value = 228437266
        difference = 228437265
        expected_long = 1
        # When
        actual_long = self.math_utils.subtract(base_value, difference)
        # Then
        self.assertEqual(expected_long, actual_long)
    
    def test_float_subtraction(self):
        # Given
        base_value = 750.585
        difference = 795.0
        expected_float = -44.415
        # When
        actual_float = self.math_utils.subtract(base_value, difference)
        # Then
        self.assertAlmostEqual(expected_float, actual_float, places=2)
    
    def test_double_subtraction(self):
        # Given
        base_value = 225.25
        difference = 231
        expected_double = -5.75
        # When
        actual_double = self.math_utils.subtract(base_value, difference)
        # Then
        self.assertEqual(expected_double, actual_double)

if __name__ == '__main__':
    unittest.main()