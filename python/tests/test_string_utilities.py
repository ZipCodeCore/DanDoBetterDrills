"""
Modified by kristofer 3/4/2024.
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import unittest
from danny_do_better_exercises.string_utilities import StringUtilities

class TestStringUtilities(unittest.TestCase):
    
    def test_get_hello_world(self):
        # Given
        expected = "Hello World"
        
        # When
        actual = StringUtilities.get_hello_world()
        
        # Then
        self.assertEqual(expected, actual)
    
    def test_concatenation_string(self):
        # Given
        one = "Hello"
        two = " Java"
        expected = "Hello Java"
        
        # When
        actual = StringUtilities.concatenation(one, two)
        
        # Then
        self.assertEqual(expected, actual)
    
    def test_concatenation_string_and_integer(self):
        # Given
        one = 1
        two = " Java"
        expected = "1 Java"
        
        # When
        actual = StringUtilities.concatenation(one, two)
        
        # Then
        self.assertEqual(expected, actual)
    
    def test_substring_begin(self):
        # Given
        input_str = "Hello"
        expected = "Hel"
        
        # When
        actual = StringUtilities.get_prefix(input_str)
        
        # Then
        self.assertEqual(expected, actual)
    
    def test_substring_end(self):
        # Given
        input_str = "Hello"
        expected = "llo"
        
        # When
        actual = StringUtilities.get_suffix("Hello")
        
        # Then
        self.assertEqual(expected, actual)
    
    def test_compare_to_equals(self):
        # Given
        input_value = "Zipcode"
        comparable_value = "Zipcode"
        
        # When
        actual = StringUtilities.compare_two_strings(input_value, comparable_value)
        
        # Then
        self.assertTrue(actual)
    
    def test_compare_to_not_equals(self):
        # Given
        input_value = "Zipcode"
        comparable_value = "Zipcodee"
        
        # When
        actual = StringUtilities.compare_two_strings(input_value, comparable_value)
        
        # Then
        self.assertFalse(actual)
    
    def test_get_the_middle_char_of_zipcode(self):
        # Given
        input_str = "Zipcode"
        expected = 'c'
        
        # When
        actual = StringUtilities.get_middle_character(input_str)
        
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_the_middle_char_of_zipcoder(self):
        # Given
        input_str = "Zipcoder"
        expected = 'c'
        
        # When
        actual = StringUtilities.get_middle_character(input_str)
        
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_the_first_word(self):
        # Given
        input_str = "Zipcode Wilmington"
        expected = "Zipcode"
        
        # When
        actual = StringUtilities.get_first_word(input_str)
        
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_the_second_word(self):
        # Given
        input_str = "Zipcode Wilmington"
        expected = "Wilmington"
        
        # When
        actual = StringUtilities.get_second_word(input_str)
        
        # Then
        self.assertEqual(expected, actual)
    
    def test_reverse_them(self):
        # Given
        input_str = "Zipcode Wilmington"
        expected = "notgnimliW edocpiZ"
        
        # When
        actual = StringUtilities.reverse(input_str)
        
        # Then
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()