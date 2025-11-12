# https://github.com/chrfst/lab11-MA-CS.git
# Partner 1: Matas Ambrukaitis
# Partner 2: Christopher St. John
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(0, 7), 7)
        self.assertEqual(add(1.5, 1.5), 3)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(3, 1), 2)
        self.assertEqual(sub(-3, 1), -4)
        self.assertEqual(sub(-1, -2), 1)
        self.assertEqual(sub(0, -7), -7)
        self.assertEqual(sub(1.5, 0.5), 1)
    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-1, -2), 2)
        self.assertEqual(mul(-3, 3), -9)
        self.assertEqual(mul(0.5, 4), 2)
        self.assertEqual(mul(0, 4), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,2), 1)
        self.assertEqual(div(-2, 4), -2)
        self.assertEqual(div(2, 0), 0)

    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
         self.assertEqual(log(4, 2), 0.5)

    def test_log_invalid_base(self): # 1 assertion
         with self.assertRaises(ValueError):
             log(1, 10)
             log(-1, 10)
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(3,0)
            log(3, -1)
            log(1, 4)
            log(-2, 6)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-3, 4), 5)
        self.assertEqual(hypotenuse(3, 0), 3)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)

        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(9), 3)


# Do not touch this
if __name__ == "__main__":
    unittest.main()