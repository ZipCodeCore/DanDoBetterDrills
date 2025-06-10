"""
Modified by kristofer 3/4/2024.
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import unittest
from danny_do_better_exercises.math_utilities import MathUtilities

class TestMathUtilities(unittest.TestCase):
    def setUp(self):
        self.math_utils = MathUtilities()

if __name__ == '__main__':
    unittest.main()