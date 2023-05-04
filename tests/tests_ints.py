import unittest

import sys

sys.path.insert(0, "../../kc-polynomos")
sys.path.insert(0, "../kc-polynomos")

from polynomos.integers.callables_1 import *
from polynomos.fractions.callables import Fraction

class TestGCD(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(GCD(90, 85), 5)
        self.assertEqual(GCD(90, 0), 90)
        self.assertEqual(GCD(0, 90), 90)
        self.assertEqual(GCD(121, 33), 11)
        self.assertEqual(GCD(120, 80), 40)
        self.assertEqual(GCD(80, 120), 40)

    def test_extended_gcd(self):
        self.assertEqual(ExtendedGCD(90, 85), (5, 1, -1))
        self.assertEqual(ExtendedGCD(85, 90), (5, -1, 1))
        self.assertEqual(ExtendedGCD(80, 0), (80, 1, 0))
        self.assertEqual(ExtendedGCD(0, 80), (80, 0, 1))

class TestIntegerMembership(unittest.TestCase):
    def test_oddq(self):
        self.assertEqual(OddQ(0), False)
        self.assertEqual(OddQ(1), True)
        self.assertEqual(OddQ(2), False)

    def test_evenq(self):
        self.assertEqual(EvenQ(0), True)
        self.assertEqual(EvenQ(1), False)
        self.assertEqual(EvenQ(2), True)

    def test_intq(self):
        self.assertEqual(IntQ(0), True)
        self.assertEqual(IntQ(0.0), False)
        self.assertEqual(IntQ(25), True)
        self.assertEqual(IntQ(0.7), False)

    def test_decimalq(self):
        self.assertEqual(DecimalQ(0), False)
        self.assertEqual(DecimalQ(0.0), True)
        self.assertEqual(DecimalQ(25), False)
        self.assertEqual(DecimalQ(0.7), True)
        self.assertEqual(DecimalQ(Fraction(10, 11)), False)

    def test_numq(self):
        self.assertEqual(NumQ(21), True)
        self.assertEqual(NumQ(2.11), True)
        self.assertEqual(NumQ("111"), False)
        self.assertEqual(NumQ(Fraction(2, 5)), True)

if __name__ == '__main__':
    unittest.main()