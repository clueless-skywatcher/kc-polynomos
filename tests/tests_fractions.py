import unittest

import sys

sys.path.insert(0, "../../kc-polynomos")
sys.path.insert(0, "../kc-polynomos")

from polynomos.fractions.callables import *
from polynomos.fractions.rational import Rational
from polynomos.lists.list_callables_0 import PlainListNew

class TestFraction(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Fraction(10, 1), 10)
        self.assertEqual(Fraction(10, -1), -10)
        self.assertEqual(Fraction(10, 20), Rational(1, 2))
        self.assertEqual(Fraction(10, -20), Rational(-1, 2))
        self.assertEqual(Fraction(10, 20, auto_reduce = False), Rational(10, 20, auto_reduce=False))
        self.assertEqual(Fraction(10, -20, auto_reduce = False), Rational(-10, 20, auto_reduce=False))
        self.assertEqual(Fraction(10, 5), 2)
        self.assertEqual(Fraction(10, 5, auto_reduce = True), 2)
        self.assertRaises(ZeroDivisionError, lambda: Fraction(10, 0))
        self.assertEqual(Fraction(0, 10), 0)

    def test_add(self):
        self.assertEqual(Fraction(1, 2) + Fraction(2, 5), Fraction(9, 10))
        self.assertEqual(Fraction(1, 5) + 1, Fraction(6, 5))
        self.assertEqual(Fraction(10, 5) + 4, 6)
        self.assertEqual(Fraction(1, 10) + 0.95, Fraction(105, 100))
        self.assertEqual(Fraction(1, 10) + PlainListNew(1, 2, 3, 4, 5), PlainListNew(Fraction(11, 10), Fraction(21, 10), Fraction(31, 10), Fraction(41, 10), Fraction(51, 10)))
        self.assertEqual(1 + Fraction(1, 5), Fraction(6, 5))
        self.assertEqual(4 + Fraction(10, 5), 6)
        self.assertEqual(0.95 + Fraction(1, 10), Fraction(105, 100))
        self.assertEqual(PlainListNew(1, 2, 3, 4, 5) + Fraction(1, 10), PlainListNew(Fraction(11, 10), Fraction(21, 10), Fraction(31, 10), Fraction(41, 10), Fraction(51, 10)))

    def test_neg(self):
        self.assertEqual(Fraction(-1, 10), Rational(-1, 10))
        self.assertEqual(Fraction(1, -10), Rational(-1, 10))

    def test_rationalize(self):
        self.assertEqual(Rationalize(0.99), Rational(99, 100))
        self.assertEqual(Rationalize(-0.99), Rational(-99, 100))

    def test_mul(self):
        self.assertEqual(Fraction(10, 19) * 10, Fraction(100, 19))
        self.assertEqual(Fraction(10, 19) * 19, 10)
        self.assertEqual(Fraction(-10, 19) * 19, -10)
        self.assertEqual(Fraction(22, 45) * Fraction(2, 3), Fraction(44, 135))
        self.assertEqual(Fraction(1, 2) * Fraction(2, 5), Fraction(1, 5))

        self.assertEqual(10 * Fraction(10, 19), Fraction(100, 19))
        self.assertEqual(19 * Fraction(10, 19), 10)
        self.assertEqual(19 * Fraction(-10, 19), -10)
        
    def test_div(self):
        self.assertEqual(Fraction(10, 19) / Fraction(2, 5), Fraction(50, 38))
        self.assertEqual(Fraction(-10, 19) / Fraction(2, 5), Fraction(-50, 38))
        self.assertEqual(Fraction(1, 5) / Fraction(2, 5), Fraction(1, 2))
        self.assertEqual(Fraction(10, 8) / 10, Fraction(1, 8))
        self.assertEqual(Fraction(11, 10) / 0.99, Fraction(10, 9))
        self.assertRaises(ZeroDivisionError, lambda: Fraction(10, 11) / 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)