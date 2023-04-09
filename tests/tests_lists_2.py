import unittest

import sys

sys.path.insert(0, "../../kc-polynomos")
sys.path.insert(0, "../kc-polynomos")

from polynomos.integers.callables import EvenQ, OddQ
from polynomos.fractions.callables import Fraction
from polynomos.lists.list_callables_0 import PlainListNew
from polynomos.lists.list_callables_2 import *

class TestListOperationsII(unittest.TestCase):
    l1 = PlainListNew(1, 1, 2, 3, 1, 1, 5, 19)
    l2 = PlainListNew(1, 2, 3, 4, 5)

    def test_listcount(self):
        self.assertEqual(ListCount(self.l1, 1), 4)
        self.assertEqual(ListCount(self.l2, 1), 1)
        self.assertEqual(ListCount(self.l1, 10), 0)
        self.assertEqual(ListCount(self.l2, 10), 0)

    def test_range(self):
        self.assertEqual(Range(10), PlainListNew(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
        self.assertEqual(Range(10, 20), PlainListNew(10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
        self.assertEqual(Range(10, 20, step = 2), PlainListNew(10, 12, 14, 16, 18, 20))
        self.assertEqual(Range(10, step = 2), PlainListNew(1, 3, 5, 7, 9))
        self.assertEqual(Range(0), PlainListNew())
        self.assertEqual(Range(0, -10), PlainListNew())
        self.assertEqual(Range(0, -10, step = -1), PlainListNew(0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10))
        self.assertEqual(Range(1, 0, step = -1), PlainListNew(1, 0))
    
    def test_subdivide(self):
        from polynomos.fractions.callables import Fraction
        self.assertEqual(Subdivide(5), PlainListNew(
            0, Fraction(1, 5), Fraction(2, 5), Fraction(3, 5), Fraction(4, 5), 1
        ))
        self.assertEqual(Subdivide(5, interval = 10), 
                         PlainListNew(0, 2, 4, 6, 8, 10))
        self.assertEqual(Subdivide(5, interval = Fraction(2, 3)), PlainListNew(
            0, Fraction(2, 15), Fraction(4, 15), Fraction(6, 15), Fraction(8, 15), 
            Fraction(10, 15)
        ))
        
        self.assertEqual(Subdivide(5, interval = 5), PlainListNew(0, 1, 2, 3, 4, 5))
        self.assertEqual(Subdivide(5, interval = 6), PlainListNew(
            0, Fraction(6, 5), Fraction(12, 5), Fraction(18, 5), Fraction(24, 5), 6
        ))
        self.assertEqual(Subdivide(5, interval = 6, float_result = True), PlainListNew(
            *[round(x, 3) for x in [0, 1.20, 2.40, 3.60, 4.80, 6.00]]
        ))
        
        self.assertEqual(Subdivide(5, interval = Fraction(2, 3), float_result = True), PlainListNew(
            *[round(x, 3) for x in [0., 0.133333, 0.266667, 0.4, 0.533333, 0.666667]]
        ))

        self.assertEqual(Subdivide(5, interval = (Fraction(2, 3), Fraction(3, 4))), PlainListNew(
            Fraction(2, 3), Fraction(41, 60), Fraction(7, 10), Fraction(43, 60),
            Fraction(11, 15), Fraction(3, 4)
        ))
        self.assertEqual(Subdivide(5, interval = (Fraction(2, 3), Fraction(3, 4)), float_result = True), PlainListNew(
            *[round(x, 3) for x in [0.666667, 0.683333, 0.7, 0.716667, 0.733333, 0.75]]
        ))

        self.assertEqual(Subdivide(5, interval = 0), PlainListNew(0, 0, 0, 0, 0, 0))
        self.assertEqual(Subdivide(5, interval = (1, 1)), PlainListNew(1, 1, 1, 1, 1, 1))

        self.assertRaises(ValueError, lambda: Subdivide(5, interval=(1, 2, 3)))

    def test_prepend(self):
        self.assertEqual(Prepend(self.l1, 5), PlainListNew(5, 1, 1, 2, 3, 1, 1, 5, 19))
        self.assertEqual(Prepend(self.l1, Fraction(2, 5)), PlainListNew(Fraction(2, 5), 1, 1, 2, 3, 1, 1, 5, 19))

    def test_append(self):
        self.assertEqual(Append(self.l1, 5), PlainListNew(1, 1, 2, 3, 1, 1, 5, 19, 5))
        self.assertEqual(Append(self.l1, Fraction(2, 5)), PlainListNew(1, 1, 2, 3, 1, 1, 5, 19, Fraction(2, 5)))

    def test_insert(self):
        self.assertEqual(Insert(self.l1, 4, 4), PlainListNew(1, 1, 2, 3, 4, 1, 1, 5, 19))
        self.assertEqual(Insert(self.l1, Fraction(3, 4), 0), PlainListNew(Fraction(3, 4), 1, 1, 2, 3, 1, 1, 5, 19))
        self.assertRaises(ValueError, lambda: Insert(self.l1, 5, 20))

if __name__ == '__main__':
    unittest.main(verbosity=2)