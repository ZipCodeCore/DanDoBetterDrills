"""
Modified by kristofer 3/4/2024.
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import unittest
from danny_do_better_exercises.predicate_utilities import PredicateUtilities

class TestPredicateUtilities(unittest.TestCase):
    def setUp(self):
        self.predicate_utils = PredicateUtilities()
    
    def test_return_true(self):
        # Given
        # When
        # Then
        self.assertTrue(self.predicate_utils.return_true())
    
    def test_return_false(self):
        # Given
        # When
        # Then
        self.assertFalse(self.predicate_utils.return_false())
    
    def test_greater_than_true(self):
        # Given
        greater_value = 450
        lesser_value = 350
        
        # When
        outcome = self.predicate_utils.is_greater_than(greater_value, lesser_value)
        
        # Then
        self.assertTrue(outcome)
    
    def test_greater_than_false(self):
        # Given
        greater_value = 350
        lesser_value = 350
        
        # When
        outcome = self.predicate_utils.is_greater_than(greater_value, lesser_value)
        
        # Then
        self.assertFalse(outcome)
    
    def test_less_than_true(self):
        # Given
        greater_value = 450
        lesser_value = 350
        
        # When
        outcome = self.predicate_utils.is_less_than(greater_value, lesser_value)
        
        # Then
        self.assertFalse(outcome)
    
    def test_less_than_false(self):
        # Given
        greater_value = 450
        lesser_value = 350
        
        # When
        outcome = self.predicate_utils.is_less_than(greater_value, lesser_value)
        
        # Then
        self.assertFalse(outcome)
    
    def test_less_or_equal_true(self):
        # Given
        greater_value = 3
        lesser_value = 3
        
        # When
        outcome = self.predicate_utils.is_less_than_or_equal_to(greater_value, lesser_value)
        
        # Then
        self.assertTrue(outcome)
    
    def test_less_or_equal_false(self):
        # Given
        greater_value = 6
        lesser_value = 3
        
        # When
        outcome = self.predicate_utils.is_less_than_or_equal_to(greater_value, lesser_value)
        
        # Then
        self.assertFalse(outcome)
    
    def test_greater_or_equal_true(self):
        # Given
        greater_value = 4
        lesser_value = 4
        
        # When
        outcome = self.predicate_utils.is_greater_than_or_equal_to(greater_value, lesser_value)
        
        # Then
        self.assertTrue(outcome)
    
    def test_greater_or_equal_false(self):
        # Given
        greater_value = 8
        lesser_value = 15
        
        # When
        outcome = self.predicate_utils.is_greater_than_or_equal_to(greater_value, lesser_value)
        
        # Then
        self.assertFalse(outcome)

if __name__ == '__main__':
    unittest.main()