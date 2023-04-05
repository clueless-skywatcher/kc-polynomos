import unittest

import sys

sys.path.insert(0, "../../kc-polynomos")
sys.path.insert(0, "../kc-polynomos")

from polynomos.lists.plainlist import PlainList
from polynomos.lists.list_callables_0 import *

class TestListInitialization(unittest.TestCase):
    l = PlainListNew(1, 2, 3, 4, 5)
    empty = PlainListNew()

    def test_init(self):
        self.assertIsInstance(self.l, PlainList)
        self.assertIsInstance(self.empty, PlainList)
        self.assertEqual(self.l._list, [1, 2, 3, 4, 5])
        self.assertEqual(self.empty._list, [])

    def test_add(self):
        self.assertEqual(self.l + 1, PlainListNew(2, 3, 4, 5, 6))
        self.assertEqual(self.l + PlainListNew(2, 1, 1, 2, 0), PlainListNew(3, 3, 4, 6, 5))
        self.assertRaises(ValueError, lambda: self.l + PlainListNew(1, 2, 3))

if __name__ == '__main__':
    unittest.main()