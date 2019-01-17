import unittest
from calculator import Calculator


def setUpModule():
    print('set up module')


def tearDownModule():
    print('tear down module')


class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.calc = Calculator()

    @classmethod
    def tearDownClass(self):
        del self.calc

    def test_add(self):
        self.assertEqual(self.calc.add(2, 7), 9)
        with self.assertRaises(TypeError):
            self.calc.add("2", 7)

    # Write test methods for subtract, multiply, and divide

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)
        with self.assertRaises(TypeError):
            self.calc.subtract("2", 7)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(10, 3), 30)
        with self.assertRaises(TypeError):
            self.calc.multiply("2", 7)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        with self.assertRaises(TypeError):
            self.calc.divide("2", 7)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(1, 0)


if __name__ == '__main__':
    unittest.main()
