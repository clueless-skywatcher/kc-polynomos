import unittest

import sys

sys.path.insert(0, "../../kc-polynomos")
sys.path.insert(0, "../kc-polynomos")

from polynomos.all import *
from polynomos.polynomials.polys import Polynomial

class TestUnivariatePolynomials(unittest.TestCase):
    uni_x_1 = UnivariatePoly(PlainListNew(0, 0, 1, 1))
    uni_x_2 = UnivariatePoly(PlainListNew(1, 2, 4, 10))

    def test_univariate(self):
        self.assertIsInstance(self.uni_x_1, Polynomial)
        self.assertIsInstance(self.uni_x_2, Polynomial)
        self.assertEqual(self.uni_x_1, UnivariatePoly(PlainListNew(0, 0, 1, 1, 0, 0)))
        self.assertNotEqual(self.uni_x_1, UnivariatePoly(PlainListNew(0, 0, 1, 1, 0, 1)))
        
    def test_uni_add(self):
        self.assertEqual(self.uni_x_1 + self.uni_x_2, UnivariatePoly(PlainListNew(1, 2, 5, 11)))
        self.assertEqual(self.uni_x_1 + 0, self.uni_x_1)
        self.assertEqual(self.uni_x_1 + self.uni_x_2, self.uni_x_2 + self.uni_x_1)
        self.assertEqual(self.uni_x_1 + self.uni_x_1, 2 * self.uni_x_1)

    def test_uni_sub(self):
        self.assertEqual(self.uni_x_1 - self.uni_x_2, UnivariatePoly(PlainListNew(-1, -2, -3, -9)))
        self.assertEqual(self.uni_x_1 - 0, self.uni_x_1)
        self.assertEqual(self.uni_x_1 + self.uni_x_2, self.uni_x_2 + self.uni_x_1)
        self.assertEqual(self.uni_x_1 - self.uni_x_1, 0)
        self.assertEqual(self.uni_x_1 - self.uni_x_1 + self.uni_x_2, self.uni_x_2)
        self.assertEqual(self.uni_x_1 + self.uni_x_1 - self.uni_x_1 + 4 * self.uni_x_1, 5 * self.uni_x_1)

    def test_uni_mul(self):
        self.assertEqual(self.uni_x_1 * 0, 0)
        self.assertEqual(self.uni_x_1 * self.uni_x_2, UnivariatePoly(PlainListNew(0, 0, 1, 3, 6, 14, 10)))
        self.assertEqual(self.uni_x_1 * self.uni_x_2, self.uni_x_2 * self.uni_x_1)
        self.assertEqual(self.uni_x_1 * -self.uni_x_2, UnivariatePoly(PlainListNew(0, 0, -1, -3, -6, -14, -10)))

class TestMultivariatePolynomials(unittest.TestCase):
    mul_x_1 = MultiPoly({
        tuple({'x': 1, 'y': 2, 'z': 0}.items()): 1,
        tuple({'x': 1, 'w': 1, 'z': 1}.items()): 2,
        tuple({'y': 1, 'z': 1}.items()): -5,
        tuple({'x': 0}.items()): 11
    })
    mul_x_2 = MultiPoly({
        tuple({'x': 1, 'y': 0, 'z': 1}.items()): 1,
        tuple({'x': 0, 'w': 0, 'z': 0}.items()): 2,
        tuple({'y': 1, 'z': 1}.items()): -1,
        tuple({'x': 5, 'y': 0, 'z': 0}.items()): -7
    })
    mul_x_3 = MultiPoly({
        tuple({'x': 3, 'y': 2, 'z': 2}.items()): 10,
        tuple({'x': 0, 'w': 1, 'z': 1}.items()): 2,
        tuple({'y': 8}.items()): -5,
        tuple({'x': 0, 'y': 0, 'z': 0}.items()): 8
    })

    def test_init(self):
        self.assertIsInstance(self.mul_x_1, Polynomial)
        self.assertIsInstance(self.mul_x_2, Polynomial)
        self.assertIsInstance(self.mul_x_3, Polynomial)

class TestSymbols(unittest.TestCase):
    vars_ = Vars('x y z', delimiter = ' ')
    
    def test_vars(self):
        x, y, z = self.vars_
        
        self.assertEqual(x, Var('x'))
        self.assertEqual(y, Var('y'))
        self.assertEqual(z, Var('z'))
        self.assertNotEqual(y, x)
        
    def test_add(self):
        x, y, z = self.vars_
        
        self.assertEqual(x + y, y + x)
        self.assertEqual(x + x, 2 * x)
        self.assertEqual(x + x + 9 * x, 11 * x)
        self.assertEqual(y - y + 9 * y, 9 * y)
        self.assertEqual(y - y, 0)
        self.assertEqual(x + 0, x)
        self.assertEqual(x + y - (x + y), 0)
        self.assertEqual(x + y - (x - y), 2 * y)
        self.assertEqual(x + y + z + y + 5 * x + 6 * z, 6 * x + 2 * y + 7 * z)

    def test_mul(self):
        x, y, z = self.vars_
        
        self.assertEqual(x * y, y * x)
        self.assertEqual(x * x, UnivariatePoly(PlainListNew(0, 0, 1)))
        self.assertEqual(x * x * 2, UnivariatePoly(PlainListNew(0, 0, 2)))
        self.assertEqual(x * x * x, UnivariatePoly(PlainListNew(0, 0, 0, 1)))
        self.assertEqual(2 * x * y, MultiPoly({
            (('x', 1), ('y', 1)): 2
        }))
        self.assertEqual(2 * x * y * y * 5 + 8 * x * z, MultiPoly({
            (('x', 1), ('y', 2)): 10,
            (('x', 1), ('z', 1)): 8
        }))

if __name__ == '__main__':
    unittest.main()

