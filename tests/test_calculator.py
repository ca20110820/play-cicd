import unittest
from the_package.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        calculator = Calculator(1, 2)
        self.assertEqual(calculator.addition(), 3)

    def test_subtraction(self):
        calculator = Calculator(2, 2)
        self.assertEqual(calculator.subtraction(), 0)

    def test_multiply(self):
        calculator = Calculator(3, 2)
        self.assertEqual(calculator.multiply(), 6)

    def test_divide(self):
        calculator = Calculator(4, 2)
        self.assertEqual(calculator.divide(), 2)
    
    def test_modulo(self):
        calculator = Calculator(4, 2)
        self.assertEqual(calculator.modulo(), 0)


if __name__ == "__main__":
    unittest.main()
