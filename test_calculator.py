import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
    #     fill in code
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(233, -2), 231)
        self.assertEqual(add(0, 0), 0)
    def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################
        self.assertEqual(subtract(1, 2), -1)
        self.assertEqual(subtract(233, 2), 231)
        self.assertEqual(subtract(0, 0), 0)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
    #     fill in code
        self.assertEqual(multiply(2,3), 6)
        self.assertEqual(multiply(-1,5), -5)
        self.assertEqual(multiply(0,0), 0)
    def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################
        self.assertEqual(divide(2,12), 6)
        self.assertAlmostEqual(divide(2,7), 3.5)
        self.assertEqual(divide(1,0), 0)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
    #     fill in code
        with self.assertRaises(ZeroDivisionError):
            divide(0,2)

    def test_logarithm(self): # 3 assertions
    #     fill in code
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(14, 5), 0.61)
        self.assertAlmostEqual(logarithm(1, 10), 0.0)

    def test_log_invalid_base(self): # 1 assertion

    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
        with self.assertRaises(ValueError):
            logarithm(1, 10)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code
        with self.assertRaises(ValueError):
            logarithm(10,0)

    def test_hypotenuse(self): # 3 assertions
    #     fill in code
        self.assertAlmostEqual(hypotenuse(3,4), 5.0)
        self.assertAlmostEqual(hypotenuse(0,200), 200.0)
        self.assertAlmostEqual(hypotenuse(0,0), 0.0)
    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################
        self.assertAlmostEqual(square_root(169), 13.0)
        self.assertAlmostEqual(square_root(0), 0.0)
        with self.assertRaises(ValueError):
            square_root(-1)

# Do not touch this
if __name__ == "__main__":
    unittest.main() 