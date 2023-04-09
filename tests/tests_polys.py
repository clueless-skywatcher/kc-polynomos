import unittest

import sys

sys.path.insert(0, "../../kc-polynomos")
sys.path.insert(0, "../kc-polynomos")

from polynomos.polynomials.poly import Polynomial
from polynomos.polynomials.callables import *
from polynomos.fractions.callables import Fraction
from polynomos.lists.list_callables_0 import PlainListNew

class TestPolynomialAddition(unittest.TestCase):
    p1 = PolynomialNew(1, 0, 2, 3, 4)
    p2 = PolynomialNew(9, -3, 2, 3, 1, 1, -2)
    p3 = PolynomialNew(1, 0, 2, 3, 4, symbol = 'y')
    p4 = PolynomialNew(Fraction(-1, 4), Fraction(2, 5), 2, 3)
    p5 = PolynomialNew(1, Fraction(2, 5), 2, 3)
    
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
        self.assertEqual(str(self.p4), "-(1/4)x^3 + (2/5)x^2 + 2x + 3")
        self.assertEqual(str(self.p5), "x^3 + (2/5)x^2 + 2x + 3")

    def test_add(self):
        self.assertIsInstance(self.p1 + self.p2, Polynomial)
        self.assertEqual(PolyCoefficientList(self.p1 + self.p2, 'x'), PlainListNew(9, -3, 3, 3, 3, 4, 2))
        self.assertEqual(PolyCoefficientList(self.p1 + self.p4, 'x'), PlainListNew(1, Fraction(-1, 4), Fraction(12, 5), 5, 7))

        self.assertEqual(str(self.p1 + self.p2), "9x^6 - 3x^5 + 3x^4 + 3x^3 + 3x^2 + 4x + 2")
        self.assertEqual(str(self.p1 + self.p4), "x^4 - (1/4)x^3 + (12/5)x^2 + 5x + 7")

        self.assertRaises(ValueError, lambda: self.p1 + "ABC")
        self.assertRaises(ValueError, lambda: self.p1 + self.p3)

    def test_neg(self):
        self.assertEqual(PolyCoefficientList(-self.p1), PlainListNew(-1, 0, -2, -3, -4))
        self.assertEqual(str(-self.p1), "-x^4 - 2x^2 - 3x - 4")

    def test_sub(self):
        self.assertIsInstance(self.p1 - self.p2, Polynomial)
        self.assertEqual(PolyCoefficientList(self.p1 - self.p2), PlainListNew(-9, 3, -1, -3, 1, 2, 6))
        self.assertEqual(str(self.p1 - self.p2), "-9x^6 + 3x^5 - x^4 - 3x^3 + x^2 + 2x + 6")
        self.assertRaises(Exception, lambda: self.p1 - "ABC")

    def test_eq(self):
        self.assertEqual(self.p1, PolynomialNew(1, 0, 2, 3, 4))
        self.assertNotEqual(self.p1, PolynomialNew(1))
        self.assertEqual(self.integer, PolynomialNew(1))
        self.assertEqual(PolynomialNew(0), 0)
        self.assertNotEqual(self.p1, PolynomialNew(1, 0, 2, 3, 4, symbol = 'y'))

class TestPolynomialDivision(unittest.TestCase):
    a = PolynomialNew(3, 2, 0, 1, 5)
    b = PolynomialNew(1, 2, 3)
    
    p1 = PolynomialNew(1, 0, 2, 3, 4)
    p2 = PolynomialNew(Fraction(-1, 4), Fraction(2, 5), 2, 3)
    

    def test_div(self):
        self.assertEqual(PolynomialQuotient(self.a, self.b), PolynomialNew(3, -4, -1))
        self.assertEqual(PolynomialRemainder(self.a, self.b), PolynomialNew(15, 8))
        self.assertEqual(PolynomialQuotientRemainder(self.a, self.b), (PolynomialNew(3, -4, -1), PolynomialNew(15, 8)))
        self.assertEqual(PolynomialQuotientRemainder(self.p1, self.p2, 'x'), (
            PolynomialNew(-4, Fraction(-32, 5)), 
            PolynomialNew(Fraction(314, 25), Fraction(139, 5), Fraction(116, 5))
        ))
        self.assertEqual(PolynomialQuotientRemainder(self.p2, self.p1, 'x'), (
            PolynomialNew(0),
            PolynomialNew(Fraction(-1, 4), Fraction(2, 5), 2, 3)
        ))
        self.assertEqual(PolynomialQuotientRemainder(
            PolynomialNew(1, 0, 0, 2, 1),
            PolynomialNew(1, 0, 1),
            'x'
        ), (
            PolynomialNew(1, 0, -1),
            PolynomialNew(2, 2)
        ))

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
        self.assertEqual(PolyCoefficientList(self.p1, 'x'), PlainListNew(1, 0, 2, 3, 4))
        self.assertEqual(PolyCoefficientList(PolynomialNew(0, 0, 2, 2, 3, 8, 6), 'x'), PlainListNew(2, 2, 3, 8, 6))
        self.assertEqual(PolyCoefficientList(self.p1, 'y'), PlainListNew())
    
if __name__ == '__main__':
    unittest.main()