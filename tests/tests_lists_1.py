import unittest

import sys
sys.path.insert(0, "../../kc-polynomos")
sys.path.insert(0, "../kc-polynomos")

from polynomos.integers.callables import EvenQ, OddQ
from polynomos.lists.list_callables_0 import PlainListNew
from polynomos.lists.list_callables_1 import *

class TestListOperationsI(unittest.TestCase):
    l_even = PlainListNew(2, 9, 11, 14, 5, 18)
    l_odd = PlainListNew(1, 8, 6, 5, 7)

    l_tw1 = PlainListNew(2, 4, 6, 1, 3, 5)
    l_tw2 = PlainListNew(1, 3, 5, 2, 4, 6)

    take = PlainListNew(2, 3, 1)
    take2 = PlainListNew(2, 3)
    take3 = PlainListNew(2, 3, 10)
    empty = PlainListNew()

    def test_element_at(self):
        self.assertEqual(ElementAt(self.l_even, 3), 14)
        self.assertEqual(ElementAt(self.l_odd, 2), 6)
        self.assertRaises(ValueError, lambda: ElementAt(self.l_even, 10))
        self.assertRaises(ValueError, lambda: ElementAt(self.empty, 1))

    def test_first(self):
        self.assertEqual(First(self.l_even), 2)
        self.assertEqual(First(self.empty), None)

    def test_last(self):
        self.assertEqual(Last(self.l_odd), 7)
        self.assertEqual(Last(self.empty), None)

    def test_middle(self):
        self.assertEqual(Middle(self.l_odd), 6)
        self.assertEqual(Middle(self.l_even), PlainListNew(11, 14))
        self.assertEqual(Middle(self.empty), None)

    def test_takeN(self):
        self.assertEqual(TakeN(self.l_even, 4), PlainListNew(2, 9, 11, 14))
        self.assertEqual(TakeN(self.l_odd, 3), PlainListNew(1, 8, 6))
        self.assertRaises(ValueError, lambda: TakeN(self.l_even, 10))
        self.assertRaises(ValueError, lambda: TakeN(self.empty, 1))

    def test_dropN(self):
        self.assertEqual(DropN(self.l_odd, 4), PlainListNew(7))
        self.assertEqual(DropN(self.l_even, 3), PlainListNew(14, 5, 18))
        self.assertRaises(ValueError, lambda: DropN(self.l_even, 10))
        self.assertRaises(ValueError, lambda: DropN(self.empty, 1))

    def test_take_list(self):
        self.assertEqual(TakeList(self.l_even, self.take), PlainListNew(
            PlainListNew(2, 9), 
            PlainListNew(11, 14, 5),
            PlainListNew(18)
        ))
        self.assertEqual(TakeList(self.l_odd, self.take2), PlainListNew(
            PlainListNew(1, 8),
            PlainListNew(6, 5, 7)
        ))
        self.assertRaises(ValueError, lambda: TakeList(self.l_odd, self.take3))
        self.assertRaises(ValueError, lambda: TakeList(self.l_even, self.take3))

    def test_take_while(self):
        self.assertEqual(TakeWhile(self.l_tw1, lambda x: x % 2 == 0), PlainListNew(2, 4, 6))
        self.assertEqual(TakeWhile(self.l_tw1, lambda x: x % 2 == 1), PlainListNew())

        self.assertEqual(TakeWhile(self.l_tw2, lambda x: x % 2 == 0), PlainListNew())
        self.assertEqual(TakeWhile(self.l_tw2, lambda x: x % 2 == 1), PlainListNew(1, 3, 5))

        self.assertEqual(TakeWhile(self.l_tw1, EvenQ), PlainListNew(2, 4, 6))
        self.assertEqual(TakeWhile(self.l_tw1, OddQ), PlainListNew())

        self.assertEqual(TakeWhile(self.l_tw2, EvenQ), PlainListNew())
        self.assertEqual(TakeWhile(self.l_tw2, OddQ), PlainListNew(1, 3, 5))

if __name__ == '__main__':
    unittest.main(verbosity=2)