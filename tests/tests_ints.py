import unittest

import sys

sys.path.insert(0, "../../kc-polynomials")

from polynomos.integers.callables import ExtendedGCD

class TestGCD(unittest.TestCase):
    def test_extended_gcd(self):
        self.assertEqual(ExtendedGCD(90, 85), (5, 1, -1))
        self.assertEqual(ExtendedGCD(80, 0), (80, 1, 0))
        self.assertEqual(ExtendedGCD(0, 80), (80, 0, 1))

if __name__ == '__main__':
    unittest.main()