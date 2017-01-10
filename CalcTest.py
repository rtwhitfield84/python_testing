import unittest
from calculator import *

def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class TestCalculator(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    print('Set up class')
    # Create an instance of the calculator that can be used in all tests
    self.calculator = Calculator()

  @classmethod
  def tearDownClass(self):
    print('Tear down class')

  def test_add(self):
    self.assertEqual(self.calculator.add(2, 7), 9)

  # Write test methods for subtract, multiply, and divide
  
  def test_subtract(self):
    self.assertEqual(self.calculator.subtract(323, 300), 23)

  def test_multiply(self):
    self.assertEqual(self.calculator.multiply(9, 8), 72)

  def test_divide(self):
    self.assertEqual(self.calculator.divide(8, 2), 4)

if __name__ == '__main__':
    unittest.main()