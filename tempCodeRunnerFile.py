import unittest
from simple_calculator import SimpleCalculator

class TestingCode(unittest.TestCase):
    
    def test_addition(self):
        answer = SimpleCalculator.add(5, 9)
        expected = 15
        self.assertEqual(answer, expected)


if __name__ == "__main__":
    unittest.main()


