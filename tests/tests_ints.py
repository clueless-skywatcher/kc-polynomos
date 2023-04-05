import unittest

import sys

sys.path.insert(0, "../../kc-polynomos")
sys.path.insert(0, "../kc-polynomos")

from polynomos.integers.callables import *

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

if __name__ == '__main__':
    unittest.main()