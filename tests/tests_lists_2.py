import unittest

import sys

sys.path.insert(0, "../../kc-polynomos")
sys.path.insert(0, "../kc-polynomos")

from polynomos.integers.callables import EvenQ, OddQ
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

if __name__ == '__main__':
    unittest.main(verbosity=2)