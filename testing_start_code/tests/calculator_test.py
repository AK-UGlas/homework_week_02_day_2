import unittest
from src.calculator import add, divide, multiply, subtract

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.first_num = 5
        self.second_num = 8
    
    def test_add(self):
        self.assertEqual(13, add(self.first_num, self.second_num))

    def test_subtract(self):
        self.assertEqual(-3, subtract(self.first_num, self.second_num))

    def test_multiply(self):
        self.assertEqual(40, multiply(self.first_num, self.second_num))

    def test_divide(self):
        self.assertAlmostEqual(0.625, divide(self.first_num, self.second_num), 3)

    

    

