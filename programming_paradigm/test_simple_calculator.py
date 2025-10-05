import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, 15), 14)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(-10, 4), -14)
        self.assertEqual(self.calc.subtract(10, -4), 14)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(10, 4), 40)
        self.assertEqual(self.calc.multiply(10, 1), 10)
        self.assertEqual(self.calc.multiply(10, 0), 0)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(10, 1), 10)
        self.assertEqual(self.calc.divide(10, 0), None)
# Remember to write additional test methods for subtract, multiply, and divide.