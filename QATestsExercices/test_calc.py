import unittest
from QATestsExercices import Test


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Test.add(10, 5), 15)
        self.assertEqual(Test.add(-1, 1), 0)
        self.assertEqual(Test.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(Test.subtract(10, 5), 5)
        self.assertEqual(Test.subtract(-1, 1), -2)
        self.assertEqual(Test.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(Test.multiply(10, 5), 50)
        self.assertEqual(Test.multiply(-1, 1), -1)
        self.assertEqual(Test.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(Test.divide(10, 5), 2)
        self.assertEqual(Test.divide(-1, 1), -1)
        self.assertEqual(Test.divide(-1, -1), 1)

        self.assertRaises(ValueError, Test.divide, 10, 0)


