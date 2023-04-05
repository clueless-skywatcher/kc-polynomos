import unittest

import sys
sys.path.insert(0, "../../kc-polynomos")
sys.path.insert(0, "../kc-polynomos")

from polynomos.lists.list_callables_0 import PlainListNew
from polynomos.lists.list_callables_1 import *

class TestListOperationsI(unittest.TestCase):
    l_even = PlainListNew(2, 9, 11, 14, 5, 18)
    l_odd = PlainListNew(1, 8, 6, 5, 7)
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

if __name__ == '__main__':
    unittest.main(verbosity=2)