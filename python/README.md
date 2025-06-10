# Danny Do Better Exercises - Python Version

This is the Python version of the Java Danny Do Better exercises lab. It contains the same structure and exercises as the Java version to help beginner Python programmers learn the language.

## Structure

```
python/
├── src/
│   └── danny_do_better_exercises/
│       ├── __init__.py
│       ├── math_utilities.py
│       ├── string_utilities.py
│       ├── predicate_utilities.py
│       └── zipcode_rocks.py
└── tests/
    ├── __init__.py
    ├── test_math_utilities.py
    ├── test_string_utilities.py
    ├── test_predicate_utilities.py
    └── math_utilities/
        ├── __init__.py
        ├── test_addition.py
        ├── test_subtraction.py
        ├── test_multiplication.py
        └── test_division.py
```

## Running Tests

To run all tests:
```bash
cd python
python -m unittest discover tests
```

To run specific test files:
```bash
cd python
python -m unittest tests.test_string_utilities
python -m unittest tests.test_predicate_utilities
python -m unittest tests.math_utilities.test_addition
```

## Exercises

The exercises involve implementing the methods in each utility class:

1. **MathUtilities** - Basic arithmetic operations (add, subtract, multiply, divide)
2. **StringUtilities** - String manipulation functions
3. **PredicateUtilities** - Boolean comparison operations
4. **ZipcodeRocks** - Simple main function

All methods currently return `None` and need to be implemented to pass the tests.