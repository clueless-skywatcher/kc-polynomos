import unittest

import sys

sys.path.insert(0, "../../kc-polynomos")

from polynomos.polynomials.poly import Polynomial
from polynomos.polynomials.callables import *

class TestPolynomialAddition(unittest.TestCase):
    p1 = PolynomialNew(1, 0, 2, 3, 4)
    p2 = PolynomialNew(9, -3, 2, 3, 1, 1, -2)
    p3 = PolynomialNew(1, 0, 2, 3, 4, symbol = 'y')

    integer = PolynomialNew(1)
        
    def test_init(self):
        self.assertIsInstance(self.p1, Polynomial)
        self.assertIsInstance(self.p2, Polynomial)
        self.assertEqual(PolyCoefficientList(self.p1, 'x'), PolyCoefficientList(PolynomialNew(0, 0, 1, 0, 2, 3, 4), 'x'))
        self.assertEqual(str(self.p1), str(PolynomialNew(0, 0, 1, 0, 2, 3, 4)))

    def test_repr(self):
        self.assertEqual(str(self.p1), "x^4 + 2x^2 + 3x + 4")
        self.assertEqual(str(self.p2), "9x^6 - 3x^5 + 2x^4 + 3x^3 + x^2 + x - 2")
        self.assertEqual(str(self.p3), "y^4 + 2y^2 + 3y + 4")

    def test_add(self):
        self.assertIsInstance(self.p1 + self.p2, Polynomial)
        self.assertEqual((self.p1 + self.p2)._coeffs, (9, -3, 3, 3, 3, 4, 2))
        self.assertEqual(str(self.p1 + self.p2), "9x^6 - 3x^5 + 3x^4 + 3x^3 + 3x^2 + 4x + 2")
        self.assertRaises(ValueError, lambda: self.p1 + "ABC")

        self.assertRaises(ValueError, lambda: self.p1 + self.p3)

    def test_neg(self):
        self.assertEqual((-self.p1)._coeffs, (-1, 0, -2, -3, -4))
        self.assertEqual(str(-self.p1), "-x^4 - 2x^2 - 3x - 4")

    def test_sub(self):
        self.assertIsInstance(self.p1 - self.p2, Polynomial)
        self.assertEqual((self.p1 - self.p2)._coeffs, (-9, 3, -1, -3, 1, 2, 6))
        self.assertEqual(str(self.p1 - self.p2), "-9x^6 + 3x^5 - x^4 - 3x^3 + x^2 + 2x + 6")
        self.assertRaises(Exception, lambda: self.p1 - "ABC")

    def test_eq(self):
        self.assertEqual(self.p1, PolynomialNew(1, 0, 2, 3, 4))
        self.assertNotEqual(self.p1, PolynomialNew(1))
        self.assertEqual(self.integer, PolynomialNew(1))
        self.assertNotEqual(self.p1, PolynomialNew(1, 0, 2, 3, 4, symbol = 'y'))

class TestPolynomialDivision(unittest.TestCase):
    a = PolynomialNew(3, 2, 0, 1, 5)
    b = PolynomialNew(1, 2, 3)

    def test_div(self):
        self.assertEqual(PolynomialQuotient(self.a, self.b), PolynomialNew(3, -4, -1))
        self.assertEqual(PolynomialRemainder(self.a, self.b), PolynomialNew(15, 8))
        self.assertEqual(PolynomialQuotientRemainder(self.a, self.b), (PolynomialNew(3, -4, -1), PolynomialNew(15, 8)))

class TestPolynomialFunctions(unittest.TestCase):
    p1 = PolynomialNew(1, 0, 2, 3, 4)
    p2 = PolynomialNew(9, -3, 2, 3, 1, 1, -2)
    p3 = PolynomialNew(1, 0, 2, 3, 4, symbol = 'y')

    def test_degree(self):
        self.assertEqual(PolynomialDegree(self.p1, 'x'), 4)
        self.assertEqual(PolynomialDegree(self.p2, 'x'), 6)
        self.assertEqual(PolynomialDegree(self.p3, 'y'), 4)
        self.assertEqual(PolynomialDegree(self.p1, 'y'), 0)
        self.assertEqual(PolynomialDegree(self.p3, 'x'), 0)
        self.assertEqual(PolynomialDegree(1, 'x'), 0),
        self.assertEqual(PolynomialDegree(8.25, 'x'), 0)

    def test_lc(self):
        self.assertEqual(PolyLeadingCoefficient(self.p1, 'x'), 1)
        self.assertEqual(PolyLeadingCoefficient(self.p2, 'x'), 9)
        self.assertEqual(PolyLeadingCoefficient(self.p1, 'y'), 0)
        self.assertEqual(PolyLeadingCoefficient(PolynomialNew(0, 0, 2, 2, 3, 8, 6), 'x'), 2)

    def test_coeff_list(self):
        self.assertEqual(PolyCoefficientList(self.p1, 'x'), [1, 0, 2, 3, 4])
        self.assertEqual(PolyCoefficientList(PolynomialNew(0, 0, 2, 2, 3, 8, 6), 'x'), [2, 2, 3, 8, 6])
        self.assertEqual(PolyCoefficientList(self.p1, 'y'), [])
    
if __name__ == '__main__':
    unittest.main()