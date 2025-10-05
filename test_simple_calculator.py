import unittest
from simple_calculator import SimpleCalculator

class TestingCode(unittest.TestCase):
    
    def test_addition(self):
        addition = SimpleCalculator()
        answer = addition.add(5, 9)
        expected = 14
        self.assertEqual(answer, expected)
    
    def test_subtraction(self):
        subtraction = SimpleCalculator()
        answer = subtraction.subtract(8, 2)
        expected = 6
        self.assertEqual(answer, expected)

    def test_multiplication(self):
        multiplication = SimpleCalculator()
        answer = multiplication.multiply(4, 3)
        expected = 12
        self.assertEqual(answer, expected)
    
    def test_division(self):
        divide = SimpleCalculator()
        answer = divide.divide(10, 2)
        expected = 5
        self.assertEqual(answer, expected)



if __name__ == "__main__":
    unittest.main()


