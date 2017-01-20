# NSS Testing the Animals & Calculator Unit Tests

## Instructions

Write test cases to verify the I/O of the following methods of `Animal` and `Dog`.

1. In the test class' `setUpClass()` method, create an instance of `Animal` and `Dog`.
1. Animal object has the correct `name` property.
1. Set a species and verify that the object property of `species` has the correct value.
1. Invoking the `walk()` method set the correct speed on the both objects.
1. The animal object is an instance of `Animal`.
1. The dog object is an instance of `Dog`.

## Test Discovery

Read the [Test Discovery section](https://docs.python.org/3.3/library/unittest.html#unittest-test-discovery) of the Python docs. It explains how you can run all tests inside a directory. This allows you to split your unit test suite into many, smaller, more maintainable modules, and the use a pattern matcher to find tests in all matching files.

```
python -m unittest discover -s . -p "Test*.py" -v
```
# Calculator Unit Tests

Just like you did in JavaScript when you learned about Jasmine, you're going to create a class that test the functionality of a Calculator class.

##### Starter code for test class

```python
import unittest
import calculator

def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class TestCalculator(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    print('Set up class')
    # Create an instance of the calculator that can be used in all tests

  @classmethod
  def tearDownClass(self):
    print('Tear down class')

  def test_add(self):
    self.assertEqual(self.calc.add(2, 7), 9)

  # Write test methods for subtract, multiply, and divide

if __name__ == '__main__':
    unittest.main()
```

##### Starter code for calculator class

```python
class Calculator():
    """Performs the four basic mathematical operations

    Methods:
     add(number, number)
     subtract(number, number)
     multiply(number, number)
     divide(number,number)
    """

    def add(self, firstOperand, secondOperand):
        """Adds two numbers together

        Arguments:
          firstOperand - Any number
          secondOperand - An number
        """

        return firstOperand + secondOperand
```

## Running the test class

```
python CalcTest.py -v
```