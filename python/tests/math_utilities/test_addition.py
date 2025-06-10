"""
@author leon on 8/26/18.
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

import unittest
from danny_do_better_exercises.math_utilities import MathUtilities

class TestAddition(unittest.TestCase):
    def setUp(self):
        self.math_utils = MathUtilities()
    
    def test_integer_addition(self):
        # Given
        base_value = 20
        added_value = 7
        expected = 27
        # When
        actual = self.math_utils.add(base_value, added_value)
        # Then
        self.assertEqual(expected, actual)
    
    def test_long_addition(self):
        # Given
        base_value = 228437266
        difference = 228437265
        expected = 456874531
        # When
        actual = self.math_utils.add(base_value, difference)
        # Then
        self.assertEqual(expected, actual)
    
    def test_float_addition(self):
        # Given
        base_value = 750.585
        added_value = 795.000
        expected = 1545.585
        # When
        actual = self.math_utils.add(base_value, added_value)
        # Then
        self.assertAlmostEqual(expected, actual, places=3)

if __name__ == '__main__':
    unittest.main()